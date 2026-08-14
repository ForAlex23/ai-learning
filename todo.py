tasks = []

while True:
    print("1 — add (добавить задачу)")
    print("2 — list (показать все задачи)")
    print("3 — done (отметить выполненной)")
    print("4 — quit (выход)")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("Добавление задачи")

        task_text = input("Введите задачу: ")

        task = {
            "id": len(tasks) + 1,
            "task": task_text,
            "done": False
        }

        tasks.append(task)

    elif choice == "2":
        print("Список задач")

        for task in tasks:
            print(
                f"{task['id']}. "
                f"{task['task']} - "
                f"{'Выполнено' if task['done'] else 'В работе'}"
            )

    elif choice == "3":
        print("Отметить задачу")

        task_id = int(input("Введите номер задачи: "))

        found = False

        for task in tasks:
            if task["id"] == task_id:
                found = True
                task["done"] = True
                print("Задача выполнена.")
                break

        if not found:
            print("Задача не найдена.")

    elif choice == "4":
        print("Выход из программы.")
        break

    else:
        print("Неизвестная команда.")