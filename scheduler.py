"""
Модуль 3. Планировщик задач.

Распределяет задачи по срокам выполнения
и сортирует их по приоритету.
"""


def schedule_tasks(tasks):
    """
    Отсортировать задачи по приоритету и сроку.

    :param tasks: список задач
    """
    return sorted(
        tasks,
        key=lambda task: (task.priority, task.due_date or "9999-12-31")
    )
