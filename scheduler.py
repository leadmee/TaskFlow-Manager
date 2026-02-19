from .task_model import Task

def schedule_tasks(tasks):
    print("Планировщик: объединённая версия")
    return sorted(tasks, key=lambda t: (t.priority, t.due_date or "9999-12-31"))
