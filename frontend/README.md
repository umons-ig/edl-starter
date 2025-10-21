# TaskFlow Frontend

Application React pour gérer des tâches avec un board Kanban.

## 🚀 Démarrage Rapide

### Prérequis

**⚠️ IMPORTANT : Le backend doit être lancé avant le frontend !**

### Étape 1 : Lancer le Backend (Terminal 1)

```bash
# Depuis la racine du projet
cd backend
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv sync
uv run uvicorn src.app:app --reload
```

Le backend sera disponible sur `http://localhost:8000`

### Étape 2 : Lancer le Frontend (Terminal 2)

```bash
# Depuis la racine du projet
cd frontend
npm install
npm run dev
```

Le frontend sera disponible sur `http://localhost:3000`

---

## 📋 Commandes Disponibles

```bash
# Développement
npm run dev              # Lancer l'application en mode dev

# Tests
npm test                 # Lancer les tests
npm run test:coverage    # Lancer les tests avec couverture

# Build
npm run build            # Construire pour la production
npm run preview          # Prévisualiser le build de production

# Linting
npm run lint             # Vérifier le code avec ESLint
```

---

## 🏗️ Structure du Projet

```
frontend/
├── src/
│   ├── components/
│   │   ├── KanbanBoard.tsx    # Board Kanban avec 3 colonnes
│   │   ├── TaskCard.tsx       # Carte de tâche individuelle
│   │   └── TaskForm.tsx       # Formulaire de création/édition
│   ├── api/
│   │   └── api.ts             # Appels API vers le backend
│   ├── types/
│   │   └── index.ts           # Types TypeScript
│   ├── test/
│   │   └── setup.ts           # Configuration des tests
│   ├── App.tsx                # Composant principal
│   ├── main.tsx               # Point d'entrée
│   └── index.css              # Styles globaux
├── package.json
├── vite.config.ts             # Configuration Vite + proxy
└── vitest.config.ts           # Configuration des tests
```

---

## 🔧 Configuration du Proxy

Le frontend utilise Vite pour rediriger automatiquement les appels API :

- Frontend : `http://localhost:3000`
- Backend : `http://localhost:8000`
- Proxy : `/api/*` → `http://localhost:8000/*`

**Exemple :**
- Frontend appelle : `fetch('/api/tasks')`
- Vite redirige vers : `http://localhost:8000/tasks`

---

## 🧪 Tests

Le projet utilise **Vitest** et **React Testing Library**.

### Lancer les tests

```bash
npm test           # Mode watch
npm test -- --run  # Une seule fois
```

### Voir la couverture

```bash
npm run test:coverage
```

Ouvrir le rapport HTML :
```bash
open coverage/index.html  # macOS
start coverage/index.html # Windows
```

---

## 📚 Technologies Utilisées

- **React 18** - Framework UI
- **TypeScript** - Typage statique
- **Tailwind CSS** - Styling
- **React Query** - Gestion d'état async et cache
- **Vite** - Build tool et dev server
- **Vitest** - Framework de tests
- **React Testing Library** - Tests de composants

---

## 🎯 Fonctionnalités

- ✅ Board Kanban avec 3 colonnes (À Faire, En Cours, Terminé)
- ✅ Créer, éditer, supprimer des tâches
- ✅ Filtrage par statut et priorité
- ✅ Gestion optimiste des mises à jour (React Query)
- ✅ Messages d'erreur si backend indisponible

---

## 🐛 Dépannage

### "Unable to connect to the backend API"

**Problème :** Le backend n'est pas lancé.

**Solution :**
```bash
# Terminal 1 - Lancez le backend
cd backend
uv run uvicorn src.app:app --reload
```

### "Module not found"

**Problème :** Dépendances pas installées.

**Solution :**
```bash
npm install
```

### Tests échouent

**Solution :**
```bash
# Réinstaller les dépendances
rm -rf node_modules package-lock.json
npm install

# Relancer les tests
npm test
```

---

## 📖 Ressources

- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Vitest Documentation](https://vitest.dev/)
- [React Query Documentation](https://tanstack.com/query/latest)
- [Tailwind CSS Documentation](https://tailwindcss.com/)

---

**Bon développement !** 🚀
