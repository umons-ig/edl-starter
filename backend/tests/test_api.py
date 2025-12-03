"""
Tests API TaskFlow - Atelier 1 Starter

Apprenez en faisant ! Ce fichier vous montre comment écrire des tests, puis vous en écrirez de similaires.

Structure de chaque test :
1. ARRANGE - Préparer les données de test
2. ACT - Faire la requête API
3. ASSERT - Vérifier la réponse
"""

import pytest


# =============================================================================
# PARTIE 1 : TESTS EXEMPLES (Apprenez de ceux-ci !)
# =============================================================================

def test_root_endpoint(client):
    """
    EXEMPLE : Tester un point de terminaison GET simple.

    Ce test vous montre le pattern de base :
    1. Faire une requête avec client.get()
    2. Vérifier le code de statut
    3. Vérifier les données de la réponse
    """
    # ACT : Faire une requête GET
    response = client.get("/")

    # ASSERT : Vérifier la réponse
    assert response.status_code == 200
    assert "Welcome to TaskFlow API" in response.json()["message"]


def test_health_check(client):
    """EXEMPLE : Un autre test de point de terminaison GET simple."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_task(client):
    """
    EXEMPLE : Tester un point de terminaison POST (création de données).

    Pattern pour les requêtes POST :
    1. Préparer les données comme un dictionnaire Python
    2. Les envoyer avec client.post()
    3. Vérifier le code de statut (201 = Créé)
    4. Vérifier les données retournées
    """
    # ARRANGE : Préparer les données
    new_task = {
        "title": "Acheter des courses",
        "description": "Lait, œufs, pain"
    }

    # ACT : Envoyer la requête POST
    response = client.post("/tasks", json=new_task)

    # ASSERT : Vérifier la réponse
    assert response.status_code == 201  # 201 = Créé

    task = response.json()
    assert task["title"] == "Acheter des courses"
    assert task["description"] == "Lait, œufs, pain"
    assert task["status"] == "todo"  # Valeur par défaut
    assert "id" in task  # Le serveur génère un ID


def test_list_tasks(client):
    """
    EXEMPLE : Tester GET avec préparation de données.

    Parfois vous devez créer des données d'abord, puis tester leur listage.
    """
    # ARRANGE : Créer quelques tâches d'abord
    client.post("/tasks", json={"title": "Tâche 1"})
    client.post("/tasks", json={"title": "Tâche 2"})

    # ACT : Obtenir la liste des tâches
    response = client.get("/tasks")

    # ASSERT : Vérifier qu'on a bien les deux tâches
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == len(tasks)


def test_get_task_by_id(client):
    """
    EXEMPLE : Tester GET pour une ressource spécifique.

    Pattern :
    1. Créer une tâche d'abord
    2. Obtenir son ID depuis la réponse
    3. Utiliser cet ID pour récupérer la tâche
    """
    # ARRANGE : Créer une tâche
    create_response = client.post("/tasks", json={"title": "Trouve-moi"})
    task_id = create_response.json()["id"]

    # ACT : Obtenir la tâche spécifique
    response = client.get(f"/tasks/{task_id}")

    # ASSERT : Vérifier qu'on a la bonne tâche
    assert response.status_code == 200
    assert response.json()["title"] == "Trouve-moi"


# =============================================================================
# PARTIE 2 : À VOUS ! Complétez ces tests
# =============================================================================

# EXERCICE 1 : Écrire un test pour SUPPRIMER une tâche
# Pattern : Créer → Supprimer → Vérifier qu'elle a disparu

# =============================================================================
# EXERCICE 1 : SUPPRESSION
# =============================================================================


def test_delete_task(client):
    """
    Test complet de suppression : Créer -> Supprimer -> Vérifier 404.
    """
    # 1. Créer une tâche
    new_task = {
        "title": "Task to delete",
        "description": "delete me"
    }
    create_response = client.post("/tasks", json=new_task)
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    # 2. Supprimer la tâche
    delete_response = client.delete(f"/tasks/{task_id}")

    # 3. Vérifier le code de statut 204 (No Content)
    assert delete_response.status_code == 204

    # 4. Essayer de GET la tâche à nouveau -> doit être 404
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_task_return_404(client):
    """
    Vérifie qu'on ne peut pas supprimer une tâche qui n'existe pas.
    """
    # Utilisation d'un faux UUID
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = client.delete(f"/tasks/{fake_id}")

    assert response.status_code == 404
    # Vérifie que le message d'erreur est pertinent
    assert "not found" in response.json()["detail"].lower()


# =============================================================================
# EXERCICE 2 : MISE À JOUR
# =============================================================================

def test_update_task(client):
    """
    Test de mise à jour du titre d'une tâche.
    """
    # 1. Créer une tâche
    new_task = {
        "title": "Titre Original",
        "description": "un test"
    }
    create_response = client.post("/tasks", json=new_task)
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    # 2. Mettre à jour le titre
    update_response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Nouveau Titre"}
    )
    assert update_response.status_code == 200

    # 3. Vérifier que la réponse contient le nouveau titre
    updated_task = update_response.json()
    assert updated_task["title"] == "Nouveau Titre"

    # 4. Vérification double via un GET (bonne pratique)
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.json()["title"] == "Nouveau Titre"


# =============================================================================
# EXERCICE 3 & 4 : VALIDATION (ERROR 422)
# =============================================================================

def test_create_task_empty_title(client):
    """
    Vérifie que la création échoue si le titre est vide.
    """
    # Tentative de création avec un titre vide
    bad_task = {"title": ""}

    response = client.post("/tasks", json=bad_task)

    # FastAPI/Pydantic renvoie 422 Unprocessable Entity pour les erreurs de validation
    assert response.status_code == 422


def test_update_task_with_invalid_priority(client):
    """
    Vérifie qu'on ne peut pas mettre une priorité invalide.
    """
    # 1. Créer une tâche valide d'abord
    create_response = client.post("/tasks", json={"title": "Valid Task"})
    task_id = create_response.json()["id"]

    # 2. Tenter une mise à jour avec une valeur non permise par l'Enum
    response = client.put(f"/tasks/{task_id}", json={"priority": "urgent"})

    # 3. Doit échouer avec 422
    assert response.status_code == 422
    # Optionnel : vérifier que le message parle de la priorité
    # assert "priority" in response.text


# =============================================================================
# TESTS DE FILTRAGE ET RECHERCHE
# =============================================================================



def test_get_nonexistent_task(client):
    """
    Vérifie le 404 sur un GET d'ID inconnu.
    """
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"/tasks/{fake_id}")
    assert response.status_code == 404


# =============================================================================
# EXERCICES BONUS
# =============================================================================

# def test_filter_tasks_by_status(client):
#     """
#     BONUS 1 : Filtrage par statut simple.
#     """
#     client.post("/tasks", json={"title": "A faire", "status": "todo"})
#     client.post("/tasks", json={"title": "Fait", "status": "done"})

#     response = client.get("/tasks?status=done")

#     assert response.status_code == 200
#     data = response.json()
 
#     assert data[0]["title"] == "Fait"
#     assert data[0]["status"] == "done"


def test_update_only_status(client):
    """
    BONUS 2 : Mise à jour partielle (PATCH-like via PUT).
    """
    # 1. Création
    create_res = client.post(
        "/tasks", json={"title": "Do not change title", "status": "todo"})
    task_id = create_res.json()["id"]

    # 2. Mise à jour SEULEMENT du statut
    update_res = client.put(f"/tasks/{task_id}", json={"status": "done"})
    assert update_res.status_code == 200

    # 3. Vérification
    updated_task = update_res.json()
    assert updated_task["status"] == "done"
    # Le titre ne doit pas changer
    assert updated_task["title"] == "Do not change title"


def test_task_lifecycle(client):
    """
    BONUS 3 : Cycle de vie complet (CRUD).
    """
    # 1. Create
    res = client.post("/tasks", json={"title": "Life Cycle Task"})
    assert res.status_code == 201
    t_id = res.json()["id"]

    # 2. Read
    res = client.get(f"/tasks/{t_id}")
    assert res.status_code == 200
    assert res.json()["title"] == "Life Cycle Task"

    # 3. Update
    res = client.put(f"/tasks/{t_id}", json={"status": "in_progress"})
    assert res.status_code == 200
    assert res.json()["status"] == "in_progress"

    # 4. Delete
    res = client.delete(f"/tasks/{t_id}")
    assert res.status_code == 204

    # 5. Verify gone
    res = client.get(f"/tasks/{t_id}")
    assert res.status_code == 404

# =============================================================================
# ASTUCES & CONSEILS
# =============================================================================


"""
PATTERNS COURANTS :

1. Tester POST (Créer) :
   response = client.post("/tasks", json={"title": "..."})
   assert response.status_code == 201

2. Tester GET (Lire) :
   response = client.get("/tasks")
   assert response.status_code == 200

3. Tester PUT (Mettre à jour) :
   response = client.put(f"/tasks/{id}", json={"title": "..."})
   assert response.status_code == 200

4. Tester DELETE (Supprimer) :
   response = client.delete(f"/tasks/{id}")
   assert response.status_code == 204

5. Tester les erreurs de validation :
   response = client.post("/tasks", json={"bad": "data"})
   assert response.status_code == 422

6. Tester les erreurs 404 :
   response = client.get("/tasks/999")
   assert response.status_code == 404

CODES DE STATUT COURANTS :
- 200 : OK (GET/PUT réussi)
- 201 : Créé (POST réussi)
- 204 : Pas de Contenu (DELETE réussi)
- 404 : Non Trouvé (la ressource n'existe pas)
- 422 : Erreur de Validation (données invalides)

RAPPELEZ-VOUS :
- La fixture `client` est automatiquement fournie par conftest.py
- La base de données est automatiquement nettoyée avant/après chaque test
- Les tests doivent être indépendants (ne pas dépendre d'autres tests)
"""


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
