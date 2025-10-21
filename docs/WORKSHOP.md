# 🎓 Workshop 1: Modern Python Testing & CI/CD

**Detailed Step-by-Step Guide**

## 📅 Workshop Overview

- **Duration:** 3 hours
- **Format:** Hands-on coding
- **Prerequisites:** Git, Python 3.11+, GitHub account

---

## Phase 1: Fork & Clone (15 min)

### 🎯 Goals
- Fork the starter repository
- Clone to your local machine
- Explore the project structure

### 📝 Steps

#### 1.1 Fork the Repository

1. Go to `https://github.com/umons/edl-starter`
2. Click the **"Fork"** button in the top right
3. Select your GitHub account as the destination

#### 1.2 Clone Your Fork

```bash
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/YOUR_USERNAME/edl-starter
cd edl-starter
```

#### 1.3 Explore the Structure

```bash
# View the directory structure
tree -L 3

# Or use ls
ls -la
ls -la backend/
ls -la backend/src/
ls -la backend/tests/
```

You should see:
```
edl-starter/
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   └── app.py           # ✅ Complete FastAPI app
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py      # ✅ Test fixtures
│   │   └── test_api.py      # ⚠️  15 tests (you'll add more)
│   └── pyproject.toml       # ✅ Complete config
├── .github/workflows/       # ⚠️  You'll add workflow here
├── docs/
└── README.md
```

### ✅ Checkpoint
- [ ] Repository forked
- [ ] Repository cloned locally
- [ ] Familiar with project structure

---

## Phase 2: UV Setup & Dependencies (15 min)

### 🎯 Goals
- Install UV (modern Python package manager)
- Create virtual environment
- Install all dependencies

### 📝 Steps

#### 2.1 Install UV

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verify installation:**
```bash
uv --version
# Should show: uv 0.4.x or higher
```

#### 2.2 Create Virtual Environment

```bash
cd backend
uv venv
```

This creates a `.venv/` directory with an isolated Python environment.

#### 2.3 Activate Virtual Environment

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt.

#### 2.4 Install Dependencies

```bash
uv sync
```

This reads `pyproject.toml` and installs:
- **Main dependencies:** fastapi, uvicorn, pydantic
- **Dev dependencies:** pytest, pytest-cov, pytest-asyncio

#### 2.5 Verify Installation

```bash
uv pip list
```

You should see packages like:
```
fastapi          0.104.1
uvicorn          0.24.0
pydantic         2.5.0
pytest           7.4.3
pytest-cov       4.1.0
...
```

### 🤔 Discussion Questions
1. **What is UV?** A modern, fast Python package manager (alternative to pip/poetry)
2. **What is `pyproject.toml`?** Standard Python project configuration file
3. **Why virtual environments?** Isolate project dependencies, avoid conflicts

### ✅ Checkpoint
- [ ] UV installed (`uv --version` works)
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`uv pip list` shows packages)

---

## Phase 3: Run the Application (15 min)

### 🎯 Goals
- Start the FastAPI server
- Explore the API documentation
- Test endpoints manually

### 📝 Steps

#### 3.1 Start the Server

```bash
uv run uvicorn src.app:app --reload
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

#### 3.2 Test the API in Browser

Open your browser and visit:

1. **Root endpoint:** http://localhost:8000
   - Should show welcome message

2. **Health check:** http://localhost:8000/health
   - Should show status: "healthy"

3. **Interactive docs:** http://localhost:8000/docs
   - Swagger UI for testing endpoints

4. **Alternative docs:** http://localhost:8000/redoc
   - ReDoc documentation

#### 3.3 Test Creating a Task (in Swagger UI)

1. Go to http://localhost:8000/docs
2. Click on **POST /tasks**
3. Click **"Try it out"**
4. Enter this JSON:
   ```json
   {
     "title": "My first task",
     "description": "Learning FastAPI",
     "priority": "high"
   }
   ```
5. Click **"Execute"**
6. You should get a `201 Created` response with the task data

#### 3.4 Test Listing Tasks

1. Click on **GET /tasks**
2. Click **"Try it out"**
3. Click **"Execute"**
4. You should see the task you just created

#### 3.5 Explore the Code

Open `backend/src/app.py` in your editor and explore:

- **Lines 27-36:** Enum definitions (TaskStatus, TaskPriority)
- **Lines 39-68:** Pydantic models (TaskBase, TaskCreate, TaskUpdate, Task)
- **Line 72:** In-memory storage (simple Python list)
- **Lines 109-118:** Root endpoint
- **Lines 161-181:** Create task endpoint
- **Lines 134-158:** List tasks with filtering

### 🤔 Discussion Questions
1. **What is Pydantic?** Data validation and serialization library
2. **What is `response_model`?** Defines the structure of the API response
3. **Why `status_code=201`?** HTTP standard for "Created" responses

### ✅ Checkpoint
- [ ] Server running without errors
- [ ] Can access http://localhost:8000/docs
- [ ] Created and retrieved a task via Swagger UI
- [ ] Understand basic code structure

---

## Phase 4: Understand Existing Tests (20 min)

### 🎯 Goals
- Understand pytest structure
- Learn about fixtures
- See test patterns

### 📝 Steps

#### 4.1 Open Test Files

```bash
# In your editor, open:
backend/tests/conftest.py
backend/tests/test_api.py
```

#### 4.2 Study `conftest.py`

This file contains **fixtures** - reusable test components.

**Key concepts:**

```python
@pytest.fixture
def client():
    """Provides a test HTTP client"""
    with TestClient(app) as test_client:
        yield test_client
```

- `@pytest.fixture` - Decorator that marks this as a fixture
- `yield` - Special pytest pattern for setup/teardown
- `client` - Tests can use this by adding `client` parameter

```python
@pytest.fixture(autouse=True)
def reset_storage():
    """Cleans database before/after each test"""
    tasks_storage.clear()  # Before test
    yield                  # Run the test
    tasks_storage.clear()  # After test
```

- `autouse=True` - Runs automatically for EVERY test
- Ensures tests don't interfere with each other

#### 4.3 Study `test_api.py`

**Test naming convention:**
- All test functions start with `test_`
- Names describe what they test

**Test structure (Arrange-Act-Assert):**

```python
def test_create_simple_task(client):
    """Creating a task with just a title should work."""

    # ACT: Make the request
    response = client.post("/tasks", json={"title": "Buy groceries"})

    # ASSERT: Check the response
    assert response.status_code == 201
    task = response.json()
    assert task["title"] == "Buy groceries"
    assert task["status"] == "todo"
    assert "id" in task
```

**Key patterns:**
- `client.post()` - Make POST request
- `client.get()` - Make GET request
- `response.status_code` - HTTP status code
- `response.json()` - Parse JSON response
- `assert` - Test assertions

#### 4.4 Run Existing Tests

```bash
# Run all tests with verbose output
uv run pytest -v
```

Expected output:
```
tests/test_api.py::test_root_endpoint PASSED
tests/test_api.py::test_health_check PASSED
tests/test_api.py::test_create_simple_task PASSED
tests/test_api.py::test_create_complete_task PASSED
tests/test_api.py::test_create_task_without_title PASSED
tests/test_api.py::test_create_task_with_empty_title PASSED
tests/test_api.py::test_list_tasks_when_empty PASSED
tests/test_api.py::test_list_tasks_with_data PASSED
tests/test_api.py::test_get_specific_task PASSED
tests/test_api.py::test_get_nonexistent_task PASSED
tests/test_api.py::test_update_task PASSED
tests/test_api.py::test_update_nonexistent_task PASSED
tests/test_api.py::test_delete_task PASSED
tests/test_api.py::test_delete_nonexistent_task PASSED

============= 14 passed in 1.23s =============
```

#### 4.5 Run a Single Test

```bash
# Run just one test
uv run pytest -v tests/test_api.py::test_create_simple_task
```

#### 4.6 Run Tests with Output

```bash
# See print statements
uv run pytest -v -s
```

### 🤔 Discussion Questions
1. **What is a fixture?** Reusable test component (setup/teardown)
2. **Why use `yield` in fixtures?** Allows cleanup after test runs
3. **Why is `reset_storage` needed?** Ensures tests are isolated and independent
4. **What does `client` fixture do?** Provides a test HTTP client for making requests

### ✅ Checkpoint
- [ ] Understand what fixtures are
- [ ] Know how to run tests (`uv run pytest -v`)
- [ ] Understand Arrange-Act-Assert pattern
- [ ] All 14 tests passing

---

## Phase 5: Write New Tests (45 min)

### 🎯 Goals
- Practice writing tests
- Test edge cases and validation
- Follow TDD principles

### 📝 Exercises

Scroll to the bottom of `backend/tests/test_api.py` - you'll see commented exercises.

#### Exercise 1: Test Invalid Priority (10 min)

**Uncomment and complete:**

```python
def test_create_task_with_invalid_priority(client):
    """Creating a task with invalid priority should fail."""
    response = client.post("/tasks", json={
        "title": "Test task",
        "priority": "urgent"  # Invalid! Should be: low, medium, high
    })

    assert response.status_code == 422  # Validation error
```

**Run your test:**
```bash
uv run pytest -v tests/test_api.py::test_create_task_with_invalid_priority
```

#### Exercise 2: Test Filter by Status (10 min)

```python
def test_filter_by_status(client):
    """Filtering tasks by status should only return matching tasks."""
    # Create tasks with different statuses
    client.post("/tasks", json={"title": "Todo task", "status": "todo"})
    client.post("/tasks", json={"title": "Done task", "status": "done"})
    client.post("/tasks", json={"title": "In progress", "status": "in_progress"})

    # Filter for done tasks
    response = client.get("/tasks?status=done")

    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Done task"
    assert tasks[0]["status"] == "done"
```

#### Exercise 3: Test Filter by Priority (10 min)

```python
def test_filter_by_priority(client):
    """Filtering tasks by priority should only return matching tasks."""
    # Create tasks with different priorities
    client.post("/tasks", json={"title": "Urgent", "priority": "high"})
    client.post("/tasks", json={"title": "Not urgent", "priority": "low"})
    client.post("/tasks", json={"title": "Normal", "priority": "medium"})

    # Filter for high priority tasks
    response = client.get("/tasks?priority=high")

    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Urgent"
    assert tasks[0]["priority"] == "high"
```

#### Exercise 4: Test Filter by Assignee (5 min)

```python
def test_filter_by_assignee(client):
    """Filtering tasks by assignee should only return their tasks."""
    # Create tasks assigned to different people
    client.post("/tasks", json={"title": "Alice task", "assignee": "alice"})
    client.post("/tasks", json={"title": "Bob task", "assignee": "bob"})

    # Filter for Alice's tasks
    response = client.get("/tasks?assignee=alice")

    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["assignee"] == "alice"
```

#### Exercise 5: Test Update Status Only (10 min)

```python
def test_update_task_status(client):
    """Updating task status should work."""
    # Create a task
    create_response = client.post("/tasks", json={
        "title": "Work in progress",
        "description": "Original description",
        "status": "todo",
        "priority": "medium"
    })
    task_id = create_response.json()["id"]

    # Update only status
    update_response = client.put(f"/tasks/{task_id}", json={
        "status": "done"
    })

    assert update_response.status_code == 200
    updated_task = update_response.json()

    # Status should be updated
    assert updated_task["status"] == "done"

    # Other fields should remain unchanged
    assert updated_task["title"] == "Work in progress"
    assert updated_task["description"] == "Original description"
    assert updated_task["priority"] == "medium"
```

#### Bonus Exercise: Test Title Length Validation

```python
def test_create_task_with_long_title(client):
    """Title longer than 200 chars should fail."""
    long_title = "a" * 201  # 201 characters

    response = client.post("/tasks", json={"title": long_title})

    assert response.status_code == 422  # Validation error
```

#### Bonus Exercise: Complete Lifecycle Test

```python
def test_complete_task_lifecycle(client):
    """Test creating, reading, updating, and deleting a task."""
    # 1. CREATE
    create_response = client.post("/tasks", json={
        "title": "Complete workflow test",
        "status": "todo"
    })
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    # 2. READ
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Complete workflow test"

    # 3. UPDATE
    update_response = client.put(f"/tasks/{task_id}", json={"status": "done"})
    assert update_response.status_code == 200
    assert update_response.json()["status"] == "done"

    # 4. DELETE
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204

    # 5. VERIFY DELETED
    final_get = client.get(f"/tasks/{task_id}")
    assert final_get.status_code == 404
```

### 🎓 TDD Principles

As you write tests, follow:

1. **RED** - Write a test that fails
2. **GREEN** - Make it pass (code already exists!)
3. **REFACTOR** - Improve test quality

### ✅ Checkpoint
- [ ] Completed at least 5 new tests
- [ ] All tests passing (`uv run pytest -v`)
- [ ] Understand test patterns
- [ ] Can write tests independently

---

## Phase 6: Test Coverage (15 min)

### 🎯 Goals
- Understand code coverage
- Generate coverage reports
- Identify untested code

### 📝 Steps

#### 6.1 Run Tests with Coverage

```bash
uv run pytest --cov
```

Expected output:
```
---------- coverage: platform darwin, python 3.11.x -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
src/__init__.py             0      0   100%
src/app.py                156     12    92%
-------------------------------------------
TOTAL                     156     12    92%
```

#### 6.2 Generate HTML Coverage Report

```bash
uv run pytest --cov --cov-report=html
```

This creates `htmlcov/` directory.

#### 6.3 View Coverage Report

```bash
# macOS/Linux
open htmlcov/index.html

# Windows
start htmlcov/index.html
```

The report shows:
- ✅ **Green lines** - Covered by tests
- ❌ **Red lines** - Not covered
- ⚠️ **Yellow lines** - Partially covered

#### 6.4 Analyze Coverage

Click on `src/app.py` to see which lines aren't tested.

Common untested lines:
- Exception handlers
- `if __name__ == "__main__"` block
- Lifespan events

**Discussion:** Should we test everything?
- Focus on business logic
- Exception handlers can be tested but aren't always critical
- 85-95% coverage is usually sufficient

### ✅ Checkpoint
- [ ] Can run coverage report
- [ ] Coverage > 85%
- [ ] Understand what coverage means
- [ ] Can identify untested code

---

## Phase 7: GitHub Actions CI/CD (40 min)

### 🎯 Goals
- Understand CI/CD concepts
- Create GitHub Actions workflow
- See automated testing in action

### 📝 Steps

#### 7.1 Create Workflow File

```bash
# Create the file
touch .github/workflows/test.yml
```

#### 7.2 Write the Workflow

Open `.github/workflows/test.yml` and add:

```yaml
name: Backend Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.11'

    - name: Install UV
      run: |
        curl -LsSf https://astral.sh/uv/install.sh | sh
        echo "$HOME/.local/bin" >> $GITHUB_PATH

    - name: Install dependencies
      run: |
        cd backend
        uv venv
        uv sync

    - name: Run tests with coverage
      run: |
        cd backend
        uv run pytest --cov --cov-report=term-missing

    - name: Check coverage threshold
      run: |
        cd backend
        uv run pytest --cov --cov-fail-under=85
```

#### 7.3 Understand the Workflow

**Trigger (`on`):**
- Runs on every push to `main`
- Runs on every pull request to `main`

**Job (`test`):**
- Runs on Ubuntu Linux
- Has 6 steps

**Steps:**
1. **Checkout** - Get the code
2. **Setup Python** - Install Python 3.11
3. **Install UV** - Install UV package manager
4. **Install dependencies** - Run `uv sync`
5. **Run tests** - Execute pytest with coverage
6. **Check threshold** - Fail if coverage < 85%

#### 7.4 Commit and Push

```bash
git status
git add .
git commit -m "Add GitHub Actions workflow and new tests"
git push origin main
```

#### 7.5 Watch the Workflow Run

1. Go to your GitHub repository
2. Click the **"Actions"** tab
3. You should see your workflow running
4. Click on the workflow to see details
5. Watch each step execute in real-time

#### 7.6 See the Results

If all goes well, you'll see:
- ✅ Green checkmarks for each step
- ✅ "All checks have passed"

If something fails:
- ❌ Red X marks the failed step
- Click on it to see error details
- Fix the issue and push again

### 🤔 Discussion Questions
1. **What is CI/CD?** Continuous Integration / Continuous Deployment
2. **Why automate testing?** Catch bugs early, ensure quality
3. **What happens if tests fail?** Workflow fails, prevents merging bad code
4. **When does this run?** Every push, every pull request

### ✅ Checkpoint
- [ ] Workflow file created
- [ ] Workflow committed and pushed
- [ ] Can see workflow in GitHub Actions tab
- [ ] All steps passing (green checkmarks)

---

## Phase 8: Verification & Discussion (15 min)

### 🎯 Goals
- Verify all learning objectives met
- Discuss key concepts
- Preview next workshop

### ✅ Final Checklist

#### Environment Setup
- [ ] UV installed and working
- [ ] Virtual environment created
- [ ] All dependencies installed

#### Application
- [ ] App runs locally
- [ ] Can access /docs endpoint
- [ ] Understand FastAPI structure

#### Testing
- [ ] All original tests passing
- [ ] 5-10 new tests written
- [ ] Understand fixtures
- [ ] Test coverage > 85%

#### CI/CD
- [ ] GitHub Actions workflow created
- [ ] Tests running automatically
- [ ] Green checkmarks on GitHub

### 🎓 Key Concepts Review

#### UV vs pip
**Traditional (pip):**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
```

**Modern (UV):**
```bash
uv venv
source .venv/bin/activate
uv sync
# Dependencies tracked in pyproject.toml automatically
```

**Benefits:**
- ✅ Faster (10-100x)
- ✅ Better dependency resolution
- ✅ Single source of truth (pyproject.toml)
- ✅ Reproducible builds

#### Test Fixtures
**Without fixtures:**
```python
def test_create_task():
    client = TestClient(app)  # Repeated
    tasks_storage.clear()      # Repeated
    # ... test code ...
```

**With fixtures:**
```python
def test_create_task(client):  # Auto-injected
    # ... test code ...
    # Cleanup automatic!
```

#### CI/CD Benefits
- ✅ **Automated testing** - Catch bugs before merge
- ✅ **Consistent environment** - Same tests everywhere
- ✅ **Team collaboration** - Shared quality standards
- ✅ **Confidence** - Safe to refactor/change code

### 🚀 What's Next?

**Workshop 2: Database Integration**
- SQLite/PostgreSQL integration
- Database migrations
- Testing with databases
- Mock vs. real databases

**Workshop 3: Deployment**
- Docker containers
- Cloud deployment (Railway/Render)
- Environment variables
- Production best practices

### 📝 Homework (Optional)

1. **Add more tests:**
   - Test filtering by multiple criteria
   - Test due date handling
   - Test description length validation

2. **Improve coverage:**
   - Get to 95%+ coverage
   - Test error handling

3. **Explore FastAPI:**
   - Add a new endpoint
   - Add request validation
   - Add response examples to docs

4. **Improve CI/CD:**
   - Add code linting (ruff/black)
   - Add security scanning
   - Cache dependencies for faster builds

### 🎉 Congratulations!

You've completed Workshop 1! You now know:
- ✅ Modern Python dependency management with UV
- ✅ Writing tests with pytest
- ✅ Test fixtures and patterns
- ✅ Code coverage analysis
- ✅ GitHub Actions for CI/CD
- ✅ Test-Driven Development principles

---

## 📚 Additional Resources

- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [pytest Documentation](https://docs.pytest.org/en/stable/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [GitHub Actions Quickstart](https://docs.github.com/en/actions/quickstart)
- [TDD Best Practices](https://martinfowler.com/bliki/TestDrivenDevelopment.html)

---

**Questions? Issues? Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) or ask your instructor!**
