"""
Модуль 10. Система уведомлений.

Отправляет напоминания о задачах и бюджете.
"""

from datetime import datetime


def deadline_warning(task):
    """
    Уведомление о дедлайне.

    :param task: объект задачи
    """
    if task.due_date:
        print(f"Срок задачи {task.title} приближается")


def budget_warning(current, limit):
    """
    Уведомление о превышении бюджета.
    """
    if current > limit:
        print("Бюджет превышен")
