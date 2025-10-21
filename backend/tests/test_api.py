"""
TaskFlow API Tests - Workshop 1 Starter

This file contains basic tests to get you started.
Your task: Add 5-10 more tests to cover edge cases and advanced scenarios!

TODO for students:
- Add test for invalid task priority
- Add test for filtering by multiple criteria
- Add test for partial updates
- Add test for title length validation
- Add more tests for edge cases you discover!
"""

import pytest


# =============================================================================
# BASIC ENDPOINT TESTS
# =============================================================================

def test_root_endpoint(client):
    """The root endpoint should return a welcome message."""
    response = client.get("/")

    assert response.status_code == 200
    assert "Welcome to TaskFlow API" in response.json()["message"]


def test_health_check(client):
    """The health endpoint should confirm the API is running."""
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


# =============================================================================
# CREATE TASK TESTS
# =============================================================================

def test_create_simple_task(client):
    """Creating a task with just a title should work."""
    response = client.post("/tasks", json={"title": "Buy groceries"})

    assert response.status_code == 201
    task = response.json()
    assert task["title"] == "Buy groceries"
    assert task["status"] == "todo"  # Default status
    assert "id" in task


def test_create_complete_task(client):
    """Creating a task with all fields should preserve all data."""
    task_data = {
        "title": "Fix authentication bug",
        "description": "Users can't log in with special characters",
        "status": "in_progress",
        "priority": "high",
        "assignee": "alice"
    }

    response = client.post("/tasks", json=task_data)

    assert response.status_code == 201
    task = response.json()
    assert task["title"] == "Fix authentication bug"
    assert task["description"] == "Users can't log in with special characters"
    assert task["status"] == "in_progress"
    assert task["priority"] == "high"
    assert task["assignee"] == "alice"


def test_create_task_without_title(client):
    """Creating a task without a title should fail."""
    response = client.post("/tasks", json={"description": "No title here"})

    assert response.status_code == 422  # Validation error


def test_create_task_with_empty_title(client):
    """Creating a task with an empty title should fail."""
    response = client.post("/tasks", json={"title": ""})

    assert response.status_code == 422


# =============================================================================
# READ TASK TESTS
# =============================================================================

def test_list_tasks_when_empty(client):
    """Listing tasks when there are none should return empty list."""
    response = client.get("/tasks")

    assert response.status_code == 200
    assert response.json() == []


def test_list_tasks_with_data(client):
    """Listing tasks should return all created tasks."""
    # Create two tasks
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})

    response = client.get("/tasks")

    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2


def test_get_specific_task(client):
    """Getting a task by ID should return that task."""
    # Create a task
    create_response = client.post("/tasks", json={"title": "Find me"})
    task_id = create_response.json()["id"]

    # Get the task
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "Find me"


def test_get_nonexistent_task(client):
    """Getting a task that doesn't exist should return 404."""
    response = client.get("/tasks/fake-id-123")

    assert response.status_code == 404


# =============================================================================
# UPDATE TASK TESTS
# =============================================================================

def test_update_task(client):
    """Updating a task should change its fields."""
    # Create a task
    create_response = client.post("/tasks", json={"title": "Original"})
    task_id = create_response.json()["id"]

    # Update it
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated"})

    assert response.status_code == 200
    assert response.json()["title"] == "Updated"


def test_update_nonexistent_task(client):
    """Updating a task that doesn't exist should return 404."""
    response = client.put("/tasks/fake-id", json={"title": "Won't work"})

    assert response.status_code == 404


# =============================================================================
# DELETE TASK TESTS
# =============================================================================

def test_delete_task(client):
    """Deleting a task should remove it."""
    # Create a task
    create_response = client.post("/tasks", json={"title": "Delete me"})
    task_id = create_response.json()["id"]

    # Delete it
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    # Verify it's gone
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_task(client):
    """Deleting a task that doesn't exist should return 404."""
    response = client.delete("/tasks/fake-id")

    assert response.status_code == 404


# =============================================================================
# TODO: ADD YOUR TESTS BELOW!
# =============================================================================

# EXERCISE 1: Test invalid priority
# def test_create_task_with_invalid_priority(client):
#     """Creating a task with invalid priority should fail."""
#     # TODO: Write this test!
#     # Hint: Try priority="urgent" (not in enum: low, medium, high)
#     pass


# EXERCISE 2: Test filtering by status
# def test_filter_by_status(client):
#     """Filtering tasks by status should only return matching tasks."""
#     # TODO: Write this test!
#     # Hint: Create tasks with different statuses, then filter
#     pass


# EXERCISE 3: Test filtering by priority
# def test_filter_by_priority(client):
#     """Filtering tasks by priority should only return matching tasks."""
#     # TODO: Write this test!
#     pass


# EXERCISE 4: Test filtering by assignee
# def test_filter_by_assignee(client):
#     """Filtering tasks by assignee should only return their tasks."""
#     # TODO: Write this test!
#     pass


# EXERCISE 5: Test updating only status
# def test_update_task_status(client):
#     """Updating task status should work."""
#     # TODO: Write this test!
#     # Hint: Create task, then update only status field
#     pass


# EXERCISE 6: Test title length validation
# def test_create_task_with_long_title(client):
#     """Title longer than 200 chars should fail."""
#     # TODO: Write this test!
#     # Hint: Create a string with 201 characters
#     pass


# EXERCISE 7: Test complete workflow
# def test_complete_task_lifecycle(client):
#     """Test creating, reading, updating, and deleting a task."""
#     # TODO: Write this test!
#     # Hint: Create → Read → Update → Delete → Verify deleted
#     pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
