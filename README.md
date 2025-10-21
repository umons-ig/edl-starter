# 🎓 EDL Workshop 1: Modern Python Testing & CI/CD

**Workshop Duration:** 3 hours
**Level:** Beginner to Intermediate
**Technologies:** Python, FastAPI, pytest, UV, GitHub Actions

## 🎯 Learning Objectives

By the end of this workshop, you will:

1. ✅ Use **UV** for modern Python dependency management
2. ✅ Write **unit tests** with pytest
3. ✅ Understand **test fixtures** and test structure
4. ✅ Configure **test coverage** reporting
5. ✅ Set up **GitHub Actions** for automated testing (CI/CD)
6. ✅ Practice **Test-Driven Development** (TDD) principles

## 📋 Prerequisites

Before starting, ensure you have:

- [ ] **Git** installed
- [ ] **Python 3.11+** installed (`python --version`)
- [ ] **GitHub account** created
- [ ] **Code editor** (VS Code recommended)
- [ ] **Terminal/Command line** familiarity

## 🚀 Quick Start

### Step 1: Fork & Clone

1. **Fork this repository** on GitHub (click "Fork" button)
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/edl-starter
   cd edl-starter
   ```

### Step 2: Install UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:
```bash
uv --version
```

### Step 3: Setup Environment

```bash
cd backend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
```

### Step 4: Run the Application

```bash
uv run uvicorn src.app:app --reload
```

Visit:
- **API:** http://localhost:8000
- **Docs:** http://localhost:8000/docs
- **Health:** http://localhost:8000/health

### Step 5: Run Tests

```bash
uv run pytest -v
```

## 📚 Workshop Structure

Follow the detailed guide in [docs/WORKSHOP.md](docs/WORKSHOP.md) for step-by-step instructions.

| Phase | Topic | Time |
|-------|-------|------|
| 1 | Fork & Setup | 15 min |
| 2 | UV & Dependencies | 15 min |
| 3 | Explore the App | 15 min |
| 4 | Understand Tests | 20 min |
| 5 | Write New Tests | 45 min |
| 6 | Test Coverage | 15 min |
| 7 | GitHub Actions | 40 min |
| 8 | Verification | 15 min |

## 🏗️ Project Structure

```
edl-starter/
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   └── app.py              # ✅ Complete FastAPI application
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py         # ✅ Test fixtures
│   │   └── test_api.py         # ⚠️  15 tests (add 5-10 more!)
│   ├── pyproject.toml          # ✅ Complete configuration
│   └── README.md
├── .github/
│   └── workflows/
│       └── .gitkeep            # ⚠️  Create test.yml here
├── docs/
│   ├── WORKSHOP.md             # 📚 Detailed instructions
│   ├── SOLUTIONS.md            # 🔒 Solutions (for instructors)
│   └── TROUBLESHOOTING.md      # 🛠️  Common issues
├── .gitignore
└── README.md                   # 👈 You are here
```

## ✅ Completion Checklist

By the end of the workshop, you should have:

- [ ] UV installed and working
- [ ] All dependencies installed with `uv sync`
- [ ] Application running locally
- [ ] All original tests passing
- [ ] 5-10 new tests written
- [ ] Test coverage > 85%
- [ ] GitHub Actions workflow created
- [ ] Tests passing on GitHub (green checkmark ✅)

## 📖 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 🆘 Getting Help

- **During workshop:** Ask your instructor
- **Issues:** Check [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
- **Questions:** Open an issue on GitHub

## 📝 License

This workshop material is provided for educational purposes.

---

**Ready to start? Head to [docs/WORKSHOP.md](docs/WORKSHOP.md) for detailed instructions!** 🚀
