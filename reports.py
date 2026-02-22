"""
Модуль 7. Отчёты и аналитика.

Формирует отчёты по задачам и финансам.
"""


def tasks_report(tasks):
    """
    Сформировать отчёт по задачам.

    :param tasks: список задач
    """
    for t in tasks:
        print(t.title, t.cost)


def total_cost_report(tasks):
    """
    Показать общую стоимость.

    :param tasks: список задач
    """
    total = sum(t.cost for t in tasks)
    print("Total:", total)
