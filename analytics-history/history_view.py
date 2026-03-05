"""
Модуль 7. Просмотр истории по временным отрезкам.

Позволяет фильтровать историю действий пользователя
по датам и периодам.
"""

from datetime import datetime


def filter_by_day(history, date):
    """
    Фильтр истории по конкретному дню.

    :param history: список записей истории
    :param date: дата
    """
    return [
        r for r in history
        if r["time"].date() == date
    ]


def filter_by_month(history, year, month):
    """
    Фильтр истории по месяцу.

    :param history: список записей
    :param year: год
    :param month: месяц
    """
    return [
        r for r in history
        if r["time"].year == year and r["time"].month == month
    ]
