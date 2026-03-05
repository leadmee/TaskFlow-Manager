"""
Модуль 5. Хранение истории.

Фиксирует изменения задач и финансовых данных.
"""

from datetime import datetime


class HistoryStore:
    """Хранилище истории."""

    def __init__(self):
        self.records = []

    def add_record(self, action, obj):
        """
        Добавить запись в историю.

        :param action: действие
        :param obj: объект изменения
        """
        self.records.append({
            "time": datetime.now(),
            "action": action,
            "object": obj
        })

    def get_history(self):
        """Получить всю историю."""
        return self.records
