"""
Модуль 5. Импорт и экспорт данных.

Отвечает за сохранение и загрузку задач и финансовых данных
между сеансами работы программы.
"""

import json


def export_tasks(tasks, filename):
    """
    Сохранить задачи в файл.

    :param tasks: список задач
    :param filename: имя файла
    """
    data = [t.__dict__ for t in tasks]

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def import_tasks(filename):
    """
    Загрузить задачи из файла.

    :param filename: имя файла
    :return: список задач
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
