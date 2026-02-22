"""
Модуль 4. Финансовые расчёты.

Выполняет расчёт стоимости задач и анализ бюджета.
"""


def calculate_task_cost(tasks):
    """
    Подсчёт общей стоимости задач.

    :param tasks: список задач
    :return: общая стоимость
    """
    return sum(t.cost for t in tasks)


def budget_forecast(tasks, limit):
    """
    Проверка превышения бюджета.

    :param tasks: список задач
    :param limit: лимит бюджета
    """
    total = calculate_task_cost(tasks)
    return total > limit
