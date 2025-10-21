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
    assert len(tasks) == 2


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
def test_delete_task(client):
    """
    VOTRE TÂCHE : Écrire un test qui supprime une tâche.

    Étapes :
    1. Créer une tâche (comme dans test_create_task)
    2. Obtenir son ID
    3. Envoyer une requête DELETE : client.delete(f"/tasks/{task_id}")
    4. Vérifier que le code de statut est 204 (No Content)
    5. Essayer de GET la tâche à nouveau → devrait retourner 404 (Not Found)

    Astuce : Regardez test_get_task_by_id pour voir comment créer et obtenir l'ID
    """
    # TODO : Écrivez votre test ici !
    pass


# EXERCICE 2 : Écrire un test pour METTRE À JOUR une tâche
# Pattern : Créer → Mettre à jour → Vérifier les changements
def test_update_task(client):
    """
    VOTRE TÂCHE : Écrire un test qui met à jour le titre d'une tâche.

    Étapes :
    1. Créer une tâche avec le titre "Titre Original"
    2. Obtenir son ID
    3. Envoyer une requête PUT : client.put(f"/tasks/{task_id}", json={"title": "Nouveau Titre"})
    4. Vérifier que le code de statut est 200
    5. Vérifier que la réponse contient le nouveau titre

    Astuce : Les requêtes PUT sont comme les POST, mais elles modifient des données existantes
    """
    # TODO : Écrivez votre test ici !
    pass


# EXERCICE 3 : Tester la validation - un titre vide devrait échouer
def test_create_task_empty_title(client):
    """
    VOTRE TÂCHE : Tester que créer une tâche avec un titre vide échoue.

    Étapes :
    1. Essayer de créer une tâche avec title = ""
    2. Vérifier que le code de statut est 422 (Erreur de Validation)

    Astuce : Regardez test_create_task, mais attendez-vous à un échec !
    """
    # TODO : Écrivez votre test ici !
    pass


# EXERCICE 4 : Tester la validation - un titre manquant devrait échouer
def test_create_task_no_title(client):
    """
    VOTRE TÂCHE : Tester que créer une tâche sans titre échoue.

    Étapes :
    1. Essayer de créer une tâche avec seulement une description, pas de titre
    2. Vérifier que le code de statut est 422 (Erreur de Validation)
    """
    # TODO : Écrivez votre test ici !
    pass


# EXERCICE 5 : Tester l'erreur 404
def test_get_nonexistent_task(client):
    """
    VOTRE TÂCHE : Tester qu'obtenir une tâche qui n'existe pas retourne 404.

    Étapes :
    1. Essayer d'obtenir une tâche avec un faux ID : client.get("/tasks/faux-id-123")
    2. Vérifier que le code de statut est 404 (Not Found)
    """
    # TODO : Écrivez votre test ici !
    pass


# =============================================================================
# EXERCICES BONUS (Si vous finissez en avance !)
# =============================================================================

# BONUS 1 : Tester le filtrage par statut
def test_filter_tasks_by_status(client):
    """
    BONUS : Tester le filtrage des tâches par statut.

    Étapes :
    1. Créer 2 tâches : une avec status="todo", une avec status="done"
    2. Obtenir les tâches avec le filtre : client.get("/tasks?status=done")
    3. Vérifier que seule la tâche "done" est retournée
    """
    # TODO : Écrivez votre test ici !
    pass


# BONUS 2 : Tester la mise à jour d'un seul champ
def test_update_only_status(client):
    """
    BONUS : Tester que mettre à jour seulement le statut ne change pas les autres champs.

    Étapes :
    1. Créer une tâche avec title="Test" et status="todo"
    2. Mettre à jour seulement le statut à "done"
    3. Vérifier que le statut a changé MAIS le titre est resté le même
    """
    # TODO : Écrivez votre test ici !
    pass


# BONUS 3 : Tester le cycle de vie complet d'une tâche
def test_task_lifecycle(client):
    """
    BONUS : Tester le cycle de vie complet : Créer → Lire → Mettre à jour → Supprimer

    Étapes :
    1. Créer une tâche
    2. La lire (GET par ID)
    3. La mettre à jour (changer le statut à "done")
    4. La supprimer
    5. Vérifier qu'elle a disparu (GET devrait retourner 404)
    """
    # TODO : Écrivez votre test ici !
    pass


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
   response = client.get("/tasks/faux-id")
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
