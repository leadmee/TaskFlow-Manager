tasks = []
task_id_counter = 1


def show_menu():
    print("\n=== Система планирования задач ===")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выход")

def add_task():
    global task_id_counter

    title = input("Название задачи: ")
    deadline = input("Срок выполнения: ")
    priority = input("Приоритет (1-5): ")

    task = {
        "id": task_id_counter,
        "title": title,
        "deadline": deadline,
        "priority": priority
    }

    tasks.append(task)
    task_id_counter += 1
    print("Задача добавлена.")
