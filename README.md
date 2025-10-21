# 🎓 EDL Atelier 1 : Tests Modernes en Python & CI/CD

**Durée de l'atelier :** 3 heures
**Niveau :** Débutant à Intermédiaire
**Technologies :** Python, FastAPI, pytest, UV, GitHub Actions

## 🎯 Objectifs d'Apprentissage

À la fin de cet atelier, vous saurez :

1. ✅ Utiliser **UV** pour la gestion moderne des dépendances Python
2. ✅ Écrire des **tests unitaires** avec pytest
3. ✅ Comprendre les **fixtures de test** et la structure des tests
4. ✅ Configurer le **reporting de couverture** de code
5. ✅ Mettre en place **GitHub Actions** pour les tests automatisés (CI/CD)
6. ✅ Pratiquer les principes du **Test-Driven Development** (TDD)

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir :

- [ ] **Git** installé
- [ ] **Python 3.11+** installé (`python --version`)
- [ ] Un **compte GitHub** créé
- [ ] Un **éditeur de code** (VS Code recommandé)
- [ ] Une familiarité avec le **terminal/ligne de commande**

## 🚀 Démarrage Rapide

### Étape 1 : Fork & Clone

1. **Forkez ce dépôt** sur GitHub (cliquez sur le bouton "Fork")
2. **Clonez votre fork :**
   ```bash
   git clone https://github.com/VOTRE_NOM_UTILISATEUR/edl-starter
   cd edl-starter
   ```

### Étape 2 : Installer UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Vérifier l'installation :
```bash
uv --version
```

### Étape 3 : Configurer l'Environnement

```bash
cd backend
uv venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
uv sync
```

### Étape 4 : Lancer l'Application

```bash
uv run uvicorn src.app:app --reload
```

Visitez :
- **API :** http://localhost:8000
- **Documentation :** http://localhost:8000/docs
- **Santé :** http://localhost:8000/health

### Étape 5 : Lancer les Tests

```bash
uv run pytest -v
```

## 📚 Structure de l'Atelier

Suivez le guide détaillé dans [docs/WORKSHOP.md](docs/WORKSHOP.md) pour les instructions pas à pas.

| Phase | Sujet | Durée |
|-------|-------|-------|
| 1 | Fork & Configuration | 15 min |
| 2 | UV & Dépendances | 15 min |
| 3 | Explorer l'Application | 15 min |
| 4 | Comprendre les Tests | 20 min |
| 5 | Écrire de Nouveaux Tests | 45 min |
| 6 | Couverture de Code | 15 min |
| 7 | GitHub Actions | 40 min |
| 8 | Vérification | 15 min |

## 🏗️ Structure du Projet

```
edl-starter/
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   └── app.py              # ✅ Application FastAPI complète
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py         # ✅ Fixtures de test
│   │   └── test_api.py         # ⚠️  15 tests (ajoutez-en 5-10 de plus !)
│   ├── pyproject.toml          # ✅ Configuration complète
│   └── README.md
├── .github/
│   └── workflows/
│       └── .gitkeep            # ⚠️  Créez test.yml ici
├── docs/
│   ├── WORKSHOP.md             # 📚 Instructions détaillées
│   ├── SOLUTIONS.md            # 🔒 Solutions (pour les instructeurs)
│   └── TROUBLESHOOTING.md      # 🛠️  Problèmes courants
├── .gitignore
└── README.md                   # 👈 Vous êtes ici
```

## ✅ Liste de Vérification d'Achèvement

À la fin de l'atelier, vous devriez avoir :

- [ ] UV installé et fonctionnel
- [ ] Toutes les dépendances installées avec `uv sync`
- [ ] L'application qui fonctionne localement
- [ ] Tous les tests originaux qui passent
- [ ] 5-10 nouveaux tests écrits
- [ ] Une couverture de tests > 85%
- [ ] Un workflow GitHub Actions créé
- [ ] Les tests qui passent sur GitHub (coche verte ✅)

## 📖 Ressources Supplémentaires

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation pytest](https://docs.pytest.org/)
- [Documentation UV](https://docs.astral.sh/uv/)
- [Documentation GitHub Actions](https://docs.github.com/fr/actions)

## 🆘 Besoin d'Aide

- **Pendant l'atelier :** Demandez à votre instructeur
- **Problèmes :** Consultez [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
- **Questions :** Ouvrez une issue sur GitHub

## 📝 Licence

Ce matériel d'atelier est fourni à des fins éducatives.

---

**Prêt à commencer ? Rendez-vous sur [docs/WORKSHOP.md](docs/WORKSHOP.md) pour les instructions détaillées !** 🚀
