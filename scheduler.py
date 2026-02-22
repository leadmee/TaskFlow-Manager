"""
Модуль 3. Планировщик задач.

Отвечает за сортировку задач по приоритету и сроку.
"""

from core.task_model import Task


def schedule_tasks(tasks):
    """
    Отсортировать задачи.

    :param tasks: список задач
    """
    return sorted(tasks, key=lambda t: (t.priority, t.due_date or "9999-12-31"))
