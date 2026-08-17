import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "tasks.json")

def load_tasks():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def add_task(tasks):
    print("Добавление задачи")
    task_text = input("Введите задачу: ").strip()
    if not task_text:
        print("Задача не может быть пустой.")
        return
    task = {
        "id": len(tasks) + 1,
        "task": task_text,
        "done": False
        }
    tasks.append(task)
    save_tasks(tasks)
    print("Задача добавлена.")

def list_tasks(tasks):
    if not tasks:
        print("Нет задач.")
        return
    for task in tasks:
        status = "Выполнено" if task["done"] else "В работе"
        print(f"{task['id']}. {task['task']} - {status}")

def done_task(tasks):
    if not tasks:
        print("Нет задач.")
        return
    task_id = int(input("Введите номер задачи: "))
    if not task_id:
        print("Номер задачи не может быть пустым.")
        return
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print("Задача выполнена.")
            return
    print("Задача не найдена.")

def quit_program():
    print("Выход из программы.")
    exit()

def unknown_command():
    print("Неизвестная команда.")

def main():
    tasks = load_tasks()
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
        else:
            unknown_command()

if __name__ == "__main__":
    main()