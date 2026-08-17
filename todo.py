def add_task(tasks):
    print("Добавление задачи")
    task_text = input("Введите задачу: ")
    task = {
        "id": len(tasks) + 1,
        "task": task_text,
        "done": False
    }
    tasks.append(task)
    print("Задача добавлена.")

def list_tasks(tasks):
    print("Список задач")
    for task in tasks:
        print(f"{task['id']}. {task['task']} - {'Выполнено' if task['done'] else 'В работе'}")

def done_task(tasks):
    print("Отметить задачу")
    task_id = int(input("Введите номер задачи: "))
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print("Задача выполнена.")
            break
    else:
        print("Задача не найдена.")

def quit_program():
    print("Выход из программы.")
    exit()

def unknown_command():
    print("Неизвестная команда.")

tasks = []

while True:
    print("1 — add (добавить задачу)")
    print("2 — list (показать все задачи)")
    print("3 — done (отметить выполненной)")
    print("4 — quit (выход)")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        list_tasks(tasks)

    elif choice == "3":
        done_task(tasks)

    elif choice == "4":
        quit_program()
        break

    else:
        unknown_command()
