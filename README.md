# 🎓 EDL - Ateliers de Développement Logiciel

**Dépôt des ateliers pratiques pour apprendre les tests, CI/CD et le développement fullstack moderne.**

---

## 📂 Structure du Projet

Ce dépôt contient **trois ateliers progressifs** :

### 📘 Atelier 1 : Backend (Python/FastAPI)
- **Dossier :** `backend/`
- **Durée :** 3 heures
- **Focus :** TDD, tests unitaires, API REST
- **Technologies :** Python, FastAPI, pytest, UV
- **Guide :** [docs/ATELIER-1.md](docs/ATELIER-1.md)

### 📗 Atelier 2 : Frontend + CI/CD
- **Dossiers :** `frontend/` + `.github/workflows/`
- **Durée :** 3 heures
- **Focus :** **Connecter frontend au backend, tests, créer le workflow CI/CD**
- **Technologies :** React, TypeScript, Vitest, GitHub Actions
- **Guide :** [docs/ATELIER-2.md](docs/ATELIER-2.md)

### 📙 Atelier 3 : Déploiement Production
- **Durée :** 3 heures
- **Focus :** **Déployer l'application complète sur le cloud**
- **Technologies :** Render, variables d'environnement, CORS, monitoring
- **Guide :** [docs/ATELIER-3.md](docs/ATELIER-3.md)

---

## 🚀 Démarrage Rapide

### Étape 1 : Fork & Clone

1. **Forkez ce dépôt** sur GitHub (cliquez sur "Fork")
2. **Clonez votre fork :**
   ```bash
   git clone https://github.com/VOTRE_NOM_UTILISATEUR/edl-starter
   cd edl-starter
   ```

### Étape 2 : Choisir votre atelier

#### Pour l'Atelier 1 (Backend) :
```bash
cd backend/
# Suivez les instructions dans docs/ATELIER-1.md
```

#### Pour l'Atelier 2 (Frontend) :
```bash
cd frontend/
# Suivez les instructions dans docs/ATELIER-2.md
```

---

## 📘 Atelier 1 - Backend

### Objectifs d'apprentissage

1. ✅ Utiliser **UV** pour la gestion des dépendances Python
2. ✅ Écrire des **tests unitaires** avec pytest
3. ✅ Configurer la **couverture de code**
4. ✅ Mettre en place **GitHub Actions** (CI/CD)

### Démarrage rapide

```bash
cd backend

# Installer UV
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# OU
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# Configurer l'environnement
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv sync

# Lancer l'application
uv run uvicorn src.app:app --reload

# Lancer les tests
uv run pytest -v
```

**📚 Guide complet :** [docs/ATELIER-1.md](docs/ATELIER-1.md)

---

## 📗 Atelier 2 - Frontend

### Objectifs d'apprentissage

**🎯 Objectif principal : Apprendre à connecter un frontend React à un backend API**

1. ✅ **Comprendre l'architecture client-serveur** (frontend ↔ backend)
2. ✅ **Configurer et utiliser le proxy Vite** pour éviter les erreurs CORS
3. ✅ **Faire des appels API depuis React** (GET, POST, DELETE, PUT)
4. ✅ **Gérer les états asynchrones** avec React Query
5. ✅ **Écrire des tests** qui mockent les appels API
6. ✅ **Debugger les problèmes** de connexion

### Démarrage rapide

**⚠️ IMPORTANT : Le backend DOIT tourner avant le frontend !**

```bash
# Terminal 1 - Backend (port 8000)
cd backend
uv run uvicorn src.app:app --reload

# Terminal 2 - Frontend (port 3000)
cd frontend
npm install
npm run dev
```

**Architecture de connexion :**
```
Frontend (localhost:3000) → Vite Proxy → Backend (localhost:8000)
     /api/tasks           →              →     /tasks
```

Visitez http://localhost:3000 et ouvrez DevTools (F12) → Network pour observer les requêtes API

**Tests :**
```bash
npm test                 # Lancer les tests
npm run test:coverage    # Avec couverture
```

**📚 Guide complet :** [docs/ATELIER-2.md](docs/ATELIER-2.md)

---

## 🏗️ Architecture Complète

```
edl-starter/
├── backend/              # Atelier 1 - API FastAPI (localhost:8000)
│   ├── src/
│   │   └── app.py        # API REST avec CRUD complet
│   ├── tests/
│   │   ├── conftest.py   # Fixtures pytest
│   │   └── test_api.py   # Tests API (exemples + exercices)
│   └── pyproject.toml    # Dépendances UV
│
├── frontend/             # Atelier 2 - React App (localhost:3000)
│   ├── src/
│   │   ├── components/   # TaskCard, TaskForm, etc.
│   │   │   ├── TaskCard.test.tsx
│   │   │   └── TaskForm.test.tsx
│   │   ├── api/
│   │   │   └── api.ts    # Appels API (fetch)
│   │   ├── App.tsx
│   │   └── App.test.tsx
│   ├── vite.config.ts    # Configuration proxy (/api → :8000)
│   └── package.json
│
├── docs/
│   ├── ATELIER-1.md      # Guide Backend
│   ├── ATELIER-2.md      # Guide Frontend + Connexion
│   └── CONNEXION-BACKEND-FRONTEND.md  # Guide détaillé de connexion
│
├── .github/
│   └── workflows/
│       └── .gitkeep      # Workflows CI/CD (à créer dans les ateliers)
│
└── README.md             # 👈 Vous êtes ici
```

---

## 🎓 Ordre Recommandé

1. **Commencez par l'Atelier 1 (Backend)**
   - Apprenez les bases des tests et CI/CD
   - Créez une API REST fonctionnelle
   - Comprenez pytest et GitHub Actions

2. **Puis faites l'Atelier 2 (Frontend)**
   - **Connectez le frontend au backend** (objectif principal)
   - Comprenez le proxy Vite et les appels API
   - Observez les requêtes HTTP dans DevTools
   - Testez avec des mocks API

---

## 🆘 Besoin d'Aide ?

### Problèmes Courants

**❌ "Connection Error" dans le frontend**
- Le backend n'est pas lancé → Démarrez-le dans un terminal séparé
- Port 8000 déjà utilisé → Arrêtez l'autre processus

**❌ "CORS Error"**
- Le proxy Vite n'est pas configuré → Vérifiez `vite.config.ts`
- Le backend tourne sur un port différent → Assurez-vous qu'il est sur 8000

**❌ Tests échouent**
- Dépendances manquantes → `uv sync` (backend) ou `npm install` (frontend)
- Mocks incorrects → Vérifiez les exemples dans les fichiers de tests

### Ressources

- **Guide connexion détaillé :** [docs/CONNEXION-BACKEND-FRONTEND.md](docs/CONNEXION-BACKEND-FRONTEND.md)
- **Questions :** Ouvrez une issue sur GitHub
- **Pendant l'atelier :** Demandez à votre instructeur

---

## 📝 Licence

Ce matériel d'atelier est fourni à des fins éducatives.

---

**Prêt à commencer ? Choisissez un atelier ci-dessus !** 🚀
