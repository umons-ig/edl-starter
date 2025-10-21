# TaskFlow Backend

API de gestion de tâches basée sur FastAPI pour apprendre le TDD, pytest et le développement Python moderne.

## Démarrage Rapide

### 1. Configurer l'Environnement

```bash
# Installer UV (si ce n'est pas déjà fait)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Créer l'environnement virtuel
uv venv

# L'activer
source .venv/bin/activate  # macOS/Linux
# OU
.venv\Scripts\activate     # Windows
```

### 2. Installer les Dépendances

```bash
uv sync
```

Cela installe :
- **fastapi** - Framework web
- **uvicorn** - Serveur ASGI
- **pydantic** - Validation des données
- **pytest** - Framework de tests
- **pytest-cov** - Rapport de couverture

### 3. Lancer le Serveur

```bash
uv run uvicorn src.app:app --reload
```

Visitez :
- API : http://localhost:8000
- Documentation : http://localhost:8000/docs
- Santé : http://localhost:8000/health

### 4. Lancer les Tests

```bash
# Lancer tous les tests
uv run pytest -v

# Lancer avec la couverture
uv run pytest --cov

# Lancer un test spécifique
uv run pytest tests/test_api.py::test_create_task -v
```

## Structure du Projet

```
backend/
├── src/
│   ├── __init__.py
│   └── app.py           # Application FastAPI (complète)
├── tests/
│   ├── __init__.py
│   ├── conftest.py      # Fixtures de test
│   └── test_api.py      # Vos tests vont ici !
├── pyproject.toml       # Configuration du projet
└── README.md            # Ce fichier
```

## Points de Terminaison de l'API

| Méthode | Point de terminaison | Description |
|---------|----------------------|-------------|
| GET | `/` | Message de bienvenue |
| GET | `/health` | Vérification de santé |
| GET | `/tasks` | Lister toutes les tâches (avec filtrage) |
| POST | `/tasks` | Créer une nouvelle tâche |
| GET | `/tasks/{id}` | Obtenir une tâche par ID |
| PUT | `/tasks/{id}` | Mettre à jour une tâche |
| DELETE | `/tasks/{id}` | Supprimer une tâche |

## Modèle de Tâche

```json
{
  "id": "abc-123",
  "title": "Acheter des courses",
  "description": "Lait, œufs, pain",
  "status": "todo",
  "priority": "medium",
  "assignee": "alice",
  "due_date": null,
  "created_at": "2025-10-21T09:00:00Z",
  "updated_at": "2025-10-21T09:00:00Z"
}
```

### Validations des Champs

- **title** : Obligatoire, 1-200 caractères
- **description** : Optionnel, max 1000 caractères
- **status** : "todo", "in_progress", ou "done"
- **priority** : "low", "medium", ou "high"
- **assignee** : Optionnel, max 100 caractères

## Guide de Tests

### Structure d'un Test

Chaque test suit le pattern **Arrange-Act-Assert** :

```python
def test_exemple(client):
    # ARRANGE : Préparer les données de test
    task_data = {"title": "Test"}

    # ACT : Faire la requête
    response = client.post("/tasks", json=task_data)

    # ASSERT : Vérifier le résultat
    assert response.status_code == 201
```

### Patterns de Tests Courants

**Créer et vérifier :**
```python
response = client.post("/tasks", json={"title": "Test"})
assert response.status_code == 201
assert response.json()["title"] == "Test"
```

**Obtenir par ID :**
```python
create_resp = client.post("/tasks", json={"title": "Test"})
task_id = create_resp.json()["id"]
get_resp = client.get(f"/tasks/{task_id}")
assert get_resp.status_code == 200
```

**Mettre à jour :**
```python
update_resp = client.put(f"/tasks/{task_id}", json={"status": "done"})
assert update_resp.status_code == 200
```

**Supprimer :**
```python
delete_resp = client.delete(f"/tasks/{task_id}")
assert delete_resp.status_code == 204
```

### Vos Tâches

1. **Complétez les Exercices 1-5** dans `tests/test_api.py`
2. **Lancez tous les tests** et assurez-vous qu'ils passent
3. **Vérifiez la couverture** - visez >85%
4. **Essayez les exercices bonus** si vous finissez en avance

## Commandes Courantes

```bash
# Lancer les tests en mode verbeux
uv run pytest -v

# Lancer avec rapport de couverture
uv run pytest --cov --cov-report=html

# Lancer un fichier de test spécifique
uv run pytest tests/test_api.py -v

# Lancer un test spécifique
uv run pytest tests/test_api.py::test_create_task -v

# Afficher les instructions print
uv run pytest -v -s

# Arrêter au premier échec
uv run pytest -x
```

## Dépannage

### "Module not found"
- Assurez-vous d'avoir activé l'environnement virtuel
- Lancez `uv sync` pour installer les dépendances

### "No module named 'src'"
- Assurez-vous d'être dans le répertoire `backend/`
- Vérifiez que `src/__init__.py` existe

### Les tests ne se lancent pas
- Vérifiez que les fonctions de test commencent par `test_`
- Vérifiez que les fichiers de test commencent par `test_`
- Assurez-vous d'utiliser `uv run pytest`

### Besoin d'aide ?
- Consultez [docs/TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md)
- Demandez à votre instructeur
- Lisez attentivement les messages d'erreur !

## Prochaines Étapes

Après avoir complété cet atelier :
1. Ajoutez plus de tests (filtrage, cas limites)
2. Améliorez la couverture de tests à 95%+
3. Configurez GitHub Actions (voir [docs/WORKSHOP.md](../docs/WORKSHOP.md))
4. Explorez la documentation FastAPI : https://fastapi.tiangolo.com/

---

**Bon Tests !** 🧪
