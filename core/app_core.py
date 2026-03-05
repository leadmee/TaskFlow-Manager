"""
Модуль 1. Ядро приложения.

Отвечает за запуск системы, обработку команд пользователя
и координацию работы остальных модулей.
"""

from .task_model import Task
from .finance import calculate_task_cost


class AppCore:
    """Главный класс приложения."""

    def __init__(self):
        """Инициализация системы."""
        self.tasks = []

    def add_task(self, title, priority, cost):
        """
        Создать новую задачу.

        :param title: название задачи
        :param priority: приоритет
        :param cost: стоимость
        """
        task = Task(title, priority, cost)
        self.tasks.append(task)

    def list_tasks(self):
        """Вывести список задач."""
        for t in self.tasks:
            print(t)
