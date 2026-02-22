"""
Модуль 2. Модель задач.

Описывает структуру задачи и операции над задачами.
"""


class Task:
    """Класс задачи."""

    def __init__(self, title, priority=1, cost=0, due_date=None):
        """
        Создание задачи.

        :param title: название
        :param priority: приоритет
        :param cost: стоимость
        :param due_date: срок выполнения
        """
        self.title = title
        self.priority = priority
        self.cost = cost
        self.due_date = due_date

    def __repr__(self):
        """Строковое представление задачи."""
        return f"<Task {self.title}, priority={self.priority}>"
