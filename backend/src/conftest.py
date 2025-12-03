import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Imports depuis votre code source
from src.app import app
from src.database import Base, get_db
from src.models import TaskModel

# 1. Utiliser une base de données en mémoire pour une isolation totale
# StaticPool est nécessaire pour SQLite en mémoire avec plusieurs threads
TEST_DATABASE_URL = "sqlite:///:memory:"

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Important : bind=test_engine pour lier la session au moteur de test
TestSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(scope="session")
def setup_test_database():
    """
    Crée les tables une seule fois pour toute la session de test.
    """
    # Crée toutes les tables définies dans Base (TaskModel, etc.)
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(autouse=True)
def clear_test_data(setup_test_database):
    """
    Nettoie TOUTES les données de la table tasks avant CHAQUE test.
    autouse=True : s'exécute automatiquement sans être appelé.
    """
    db = TestSessionLocal()
    try:
        db.query(TaskModel).delete()
        db.commit()
    finally:
        db.close()


@pytest.fixture
def client(setup_test_database):
    """
    Client de test qui REMPLACE la connexion DB par la connexion de test.
    """
    def override_get_db():
        db = TestSessionLocal()
        try:
            yield db
        finally:
            db.close()

    # C'est ici que la magie opère : on dit à l'app d'utiliser override_get_db
    # au lieu du vrai get_db défini dans app.py
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    # Nettoyage après le test
    app.dependency_overrides.clear()
