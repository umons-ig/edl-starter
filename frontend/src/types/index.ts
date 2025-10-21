// Task Status
export type TaskStatus = 'todo' | 'in_progress' | 'done';

// Task Priority
export type TaskPriority = 'low' | 'medium' | 'high';

// Base Task interface
export interface Task {
  id: string;
  title: string;
  description?: string;
  status: TaskStatus;
  priority: TaskPriority;
  created_at: string;
  updated_at: string;
}

// Task creation payload
export interface TaskCreate {
  title: string;
  description?: string;
  status?: TaskStatus;
  priority?: TaskPriority;
}

// Task update payload
export interface TaskUpdate {
  title?: string;
  description?: string;
  status?: TaskStatus;
  priority?: TaskPriority;
}
