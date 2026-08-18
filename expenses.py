import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "expenses.json")


def load_expenses():    # функция загрузки расходов из файла
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):    # функция сохранения расходов в файл
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(expenses, file, ensure_ascii=False, indent=2)
    
def add_expense(expenses):    # функция добавления расхода
    amount = input("Введите сумму расхода: ")
    try:
        amount = float(amount)
        if amount <= 0:
            print("Сумма расхода должна быть больше 0")
            return
    except ValueError:
        print("Сумма расхода должна быть числом")
        return
    category = input("Введите категорию расхода: ").strip()
    if not category:
        category = "other"
    description = input("Введите описание комментария: ").strip()
    if not description:
        description = "Без описания"

    expense = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)    # добавляем расход в список
    print(f"Расход {expense['id']} добавлен успешно")
    save_expenses(expenses)    # сохраняем расходы в файл
def list_expenses(expenses):    # функция вывода всех расходов
    if not expenses:
        print("Нет расходов")
        return
    for expense in expenses:
        print(f"{expense['id']} - {expense['amount']} - {expense['category']} - {expense['description']}")

def total_expenses(expenses):    # функция вычисления общей суммы расходов
    total = 0 
    for expense in expenses:
        total += expense['amount']
    print(f"Общая сумма расходов: {total}")

def expenses_by_category(expenses):    # функция вычисления суммы расходов по категории
    category =  input("Введите категорию: ").strip()
    if not category:
        print("Категория не может быть пустой")
    total = 0
    for expense in expenses:
        if expense['category'] == category:
            total += expense['amount']
    print(f"Сумма расходов по категории {category}: {total}")

def quit_program():    # функция выхода из программы
    print("Выход из программы")
def unknown_command():    # функция вывода сообщения о неизвестной команде
    print("Неизвестная команда")

def main():    # функция запуска программы
    expenses = load_expenses()    # загружаем расходы из файла
    while True:
        print("1 — add (добавить расход)")    # выводим меню
        print("2 — list (показать все)")    # выводим меню
        print("3 — total (показать общую сумму расходов)")    # выводим меню
        print("4 — by (сумма по категории)")    # выводим меню
        print("5 — quit (выход)")    # выводим меню
        choice = input("Выберите действие: ")    # вводим команду
        if choice == "1":
            add_expense(expenses)    # добавляем расход
        elif choice == "2":
            list_expenses(expenses)    # выводим все расходы
        elif choice == "3":
            total_expenses(expenses)    # выводим общую сумму расходов
        elif choice == "4":
            expenses_by_category(expenses)    # выводим сумму по категории
        elif choice == "5":
            quit_program()    # выходим из программы
            break
        else:
            unknown_command()    # выводим сообщение о неизвестной команде
if __name__ == "__main__":
    main()    # запускаем программу