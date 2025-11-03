import { describe, it, expect, vi } from 'vitest';
import { api } from './api';

describe('API Module', () => {

  it('fetches tasks from the backend', async () => {
    (globalThis as any).fetch = vi.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve([{ id: 1, title: 'Test Task', status: 'todo' }]),
      })
    );

    const tasks = await api.getTasks();
    expect(tasks).toHaveLength(1);
    expect(tasks[0].title).toBe('Test Task');
  });

  it('creates a new task', async () => {
    const newTask = { title: 'New Task', status: 'todo' as const };

    (globalThis as any).fetch = vi.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ ...newTask, id: 1 }),
      })
    );

    const created = await api.createTask(newTask);
    expect(created.id).toBe(1);
    expect(created.title).toBe('New Task');
  });

  it('throws error when API fails', async () => {
    (globalThis as any).fetch = vi.fn(() =>
      Promise.resolve({ ok: false, status: 500, statusText: 'Server Error' })
    );

    await expect(api.getTasks()).rejects.toThrow('API error: 500 Server Error');
  });

  it('deletes a task', async () => {
    (globalThis as any).fetch = vi.fn(() =>
      Promise.resolve({ ok: true, status: 204, statusText: 'No Content' })
    );

    const deleted = await api.deleteTask(1);
    expect(globalThis.fetch).toHaveBeenCalledWith('/api/tasks/1', { method: 'DELETE', headers: { 'Content-Type': 'application/json' } });

  });

  it('updates a task', async () => {
    (globalThis as any).fetch = vi.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ id: 1, title: 'Updated Title' }),
      })
    );

    const updated = await api.updateTask(1, { title: 'Updated Title' });
    expect(globalThis.fetch).toHaveBeenCalledWith('/api/tasks/1', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title: 'Updated Title' })
    });
    expect(updated).toEqual({ id: 1, title: 'Updated Title' });
  });

}); // <-- fermeture du describe