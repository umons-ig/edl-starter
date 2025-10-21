# 🔗 Comment Relier le Backend et le Frontend

Ce guide explique comment le frontend React communique avec le backend FastAPI.

---

## 🏗️ Architecture

```
┌─────────────────────┐         ┌─────────────────────┐
│  Frontend (React)   │         │  Backend (FastAPI)  │
│  localhost:3000     │ ─────▶  │  localhost:8000     │
│                     │         │                     │
│  Vite Proxy         │         │  API REST           │
│  /api/* → :8000/*   │         │  /tasks, /health    │
└─────────────────────┘         └─────────────────────┘
```

---

## ⚙️ Configuration du Proxy Vite

### Fichier : `frontend/vite.config.ts`

```typescript
export default defineConfig({
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
})
```

**Que fait ce proxy ?**

| Frontend appelle | Vite redirige vers |
|-----------------|-------------------|
| `GET /api/tasks` | `GET http://localhost:8000/tasks` |
| `POST /api/tasks` | `POST http://localhost:8000/tasks` |
| `DELETE /api/tasks/123` | `DELETE http://localhost:8000/tasks/123` |

---

## 📡 Appels API dans le Frontend

### Fichier : `frontend/src/api/api.ts`

```typescript
// Configuration de base
const API_BASE = import.meta.env.VITE_API_URL || '/api';

// Fonction helper pour les appels
async function apiRequest<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const url = `${API_BASE}${endpoint}`;  // /api/tasks

  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }

  return response.json();
}

// Exemple : Récupérer toutes les tâches
export const api = {
  async getTasks(): Promise<Task[]> {
    return apiRequest<Task[]>('/tasks');  // GET /api/tasks
  },

  async createTask(task: TaskCreate): Promise<Task> {
    return apiRequest<Task>('/tasks', {
      method: 'POST',
      body: JSON.stringify(task),
    });
  },
};
```

---

## 🔄 Flux Complet : Créer une Tâche

### 1️⃣ Utilisateur clique sur "Créer"

**Composant :** `App.tsx`

```typescript
const createTaskMutation = useMutation({
  mutationFn: (taskData: TaskCreate) => api.createTask(taskData),
  onSuccess: () => {
    queryClient.invalidateQueries({ queryKey: ['tasks'] });
  },
});
```

### 2️⃣ React Query appelle l'API

**Fichier :** `src/api/api.ts`

```typescript
api.createTask({ title: "Ma tâche", priority: "high" })
```

### 3️⃣ Fetch fait la requête

```http
POST /api/tasks
Content-Type: application/json

{
  "title": "Ma tâche",
  "priority": "high"
}
```

### 4️⃣ Vite Proxy redirige

```
POST /api/tasks → POST http://localhost:8000/tasks
```

### 5️⃣ Backend FastAPI répond

**Fichier :** `backend/src/app.py`

```python
@app.post("/tasks", response_model=Task, status_code=201)
async def create_task(task_data: TaskCreate):
    task = Task(
        id=str(uuid4()),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        **task_data.model_dump()
    )
    tasks_storage.append(task)
    return task
```

**Réponse :**

```json
{
  "id": "abc-123",
  "title": "Ma tâche",
  "priority": "high",
  "status": "todo",
  "created_at": "2025-10-21T10:00:00Z",
  "updated_at": "2025-10-21T10:00:00Z"
}
```

### 6️⃣ React Query met à jour l'UI

```typescript
onSuccess: () => {
  // Invalide le cache → refetch automatique
  queryClient.invalidateQueries({ queryKey: ['tasks'] });
}
```

---

## 🚀 Lancer Backend + Frontend

### Terminal 1 - Backend

```bash
cd backend
source .venv/bin/activate  # Si pas déjà activé
uv run uvicorn src.app:app --reload
```

✅ Backend disponible sur `http://localhost:8000`

### Terminal 2 - Frontend

```bash
cd frontend
npm run dev
```

✅ Frontend disponible sur `http://localhost:3000`

### Vérification

1. Ouvrir http://localhost:3000
2. La page se charge correctement (pas d'erreur "Connection Error")
3. Créer une tâche
4. Vérifier dans l'onglet Network du navigateur :

```
Request URL: http://localhost:3000/api/tasks
Status: 201 Created
```

---

## 🔍 Déboguer la Connexion

### Le frontend affiche "Connection Error"

**Cause :** Le backend n'est pas lancé.

**Solution :**

```bash
cd backend
uv run uvicorn src.app:app --reload
```

### Erreur CORS

**Si vous voyez :** `Access-Control-Allow-Origin`

**Vérifiez dans `backend/src/app.py` :**

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ← Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Voir les requêtes

**Dans le navigateur :**

1. Ouvrir DevTools (F12)
2. Onglet **Network**
3. Filtrer par **Fetch/XHR**
4. Créer une tâche
5. Voir la requête `POST /api/tasks`

**Dans le terminal backend :**

```
INFO:     127.0.0.1:58392 - "POST /tasks HTTP/1.1" 201 Created
```

---

## 📚 Points Clés à Retenir

1. **Proxy Vite** redirige `/api/*` → `http://localhost:8000/*`
2. **React Query** gère le cache et les états (loading, error, success)
3. **Fetch API** fait les requêtes HTTP
4. **FastAPI** répond avec du JSON
5. **Les deux doivent tourner** en même temps

---

## 🎯 Pour l'Atelier 2

Les étudiants vont :

1. ✅ Lancer backend + frontend
2. ✅ Voir comment ils communiquent
3. ✅ Écrire des tests qui **mockent** les appels API
4. ✅ Tester l'intégration complète

---

**Questions ? Consultez [frontend/README.md](../frontend/README.md)** 🚀
