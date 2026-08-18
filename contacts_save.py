import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "contacts.json")


def load_contacts(): # функция загрузки контактов из файла
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            contacts = json.load(file)    # загружаем контакты из файла
        return contacts or []    # если contacts пустой, то возвращаем пустой список
    except FileNotFoundError:
        return []    # если файл не найден, то возвращаем пустой список

def save_contacts(contacts): # функция сохранения контактов в файл
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=2)    # сохраняем контакты в файл

def search_contact(contacts): # функция поиска контакта по имени
    print("Поиск контакта по имени")
    search_name = input("Введите имя: ").lower().strip()
    if not search_name:
        print("Имя не может быть пустым.")
        return
    found = False    # флаг для проверки найден ли контакт 

    for contact in contacts:
        if search_name in contact["name"].lower():    # если имя контакта содержит search_name, то выводим контакт
            print(f"{contact['name']} - {contact['phone']}")
            found = True    # флаг для проверки найден ли контакт

    if not found:
        print("Контакт не найден.")    # если контакт не найден, то выводим сообщение
        return False    # возвращаем False  
    else:
        return True    # возвращаем True

def delete_contact(contacts): # функция удаления контакта по имени
    print("Удаление контакта")

    delete_name = input("Введите имя: ").lower().strip()
    if not delete_name:
        print("Имя не может быть пустым.")
        return
    found = False    # флаг для проверки найден ли контакт

    i = 0    # счетчик для проверки всех контактов

    while i < len(contacts):
        if delete_name == contacts[i]["name"].lower():    # если имя контакта равно delete_name, то удаляем контакт
            contacts.pop(i)
            save_contacts(contacts)    # сохраняем контакты в файл
            found = True    # флаг для проверки найден ли контакт   
        else:
            i += 1    # увеличиваем счетчик для проверки всех контактов

    if not found:
        print("Контакт не найден.")    # если контакт не найден , то выводим сообщение
        return False    # возвращаем False
    else:
        print("Контакт удален.")    # если контакт найден, то выводим сообщение
        save_contacts(contacts)    # сохраняем контакты в файл
        return True    # возвращаем True

def list_contacts(contacts): # функция вывода всех контактов
    if len(contacts) > 0:
        print("Список всех контактов")
        for contact in contacts:
            print(f"{contact['name']} - {contact['phone']}")    # выводим имя и номер телефона контакта
    else:
        print("Список контактов пуст.")    # если список контактов пуст, то выводим сообщение
    return contacts    # возвращаем список контактов

def quit_program(): # функция выхода из программы
    print("Выход из программы.")    # выводим сообщение


def unknown_command(): # функция вывода сообщения о неизвестной команде
    print("Неизвестная команда.")    # выводим сообщение


def add_contact(contacts): # функция добавления контакта
    print("Добавление контакта")

    name = input("Введите имя: ").strip()
    if not name:
        print("Имя не может быть пустым.")
        return
    phone = input("Введите номер телефона: ").strip()
    if not phone:
        print("Номер телефона не может быть пустым.")
        return

    contact = {"name": name, "phone": phone}    # создаем контакт

    contacts.append(contact)    # добавляем контакт в список

    print("Контакт добавлен.")    # выводим сообщение
    save_contacts(contacts)    # сохраняем контакты в файл

def main():    # функция запуска программы
    contacts = load_contacts()    # загружаем контакты из файла
    while True:
        print("1 — add (добавить контакт)")    # выводим меню
        print("2 — find (найти по имени)")    # выводим меню
        print("3 — delete (удалить контакт)")    # выводим меню
        print("4 — list (показать все контакты)")    # выводим меню
        print("5 — quit (выход)")    # выводим меню
        choice = input("Выберите действие: ")    # вводим команду
        if choice == "1":
            add_contact(contacts)    # добавляем контакт
        elif choice == "2":
            search_contact(contacts)    # ищем контакт
        elif choice == "3":
            delete_contact(contacts)    # удаляем контакт
        elif choice == "4":
            list_contacts(contacts)    # выводим все контакты
        elif choice == "5":
            quit_program()    # выходим из программы
            break
        else:
            unknown_command()    # выводим сообщение о неизвестной команде  
if __name__ == "__main__":
    main()    # запускаем программу