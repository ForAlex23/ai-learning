def search_contact(contacts):
    print("Поиск контакта по имени")

    search_name = input("Введите имя: ").lower()
    found = False

    for contact in contacts:
        if search_name in contact["name"].lower():
            print(f"{contact['name']} - {contact['phone']}")
            found = True

    if not found:
        print("Контакт не найден.")


def delete_contact(contacts):
    print("Удаление контакта")

    delete_name = input("Введите имя: ").lower()
    found = False

    i = 0

    while i < len(contacts):
        if delete_name == contacts[i]["name"].lower():
            contacts.pop(i)
            found = True
        else:
            i += 1

    if not found:
        print("Контакт не найден.")
    else:
        print("Контакты удалены.")


def list_contacts(contacts):
    print("Список всех контактов")

    for contact in contacts:
        print(f"{contact['name']} - {contact['phone']}")


def quit_program():
    print("Выход из программы.")


def unknown_command():
    print("Неизвестная команда.")


def add_contact(contacts):
    print("Добавление контакта")

    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)

    print("Контакт добавлен.")


contacts = []

while True:
    print("1 — add (добавить контакт)")
    print("2 — find (найти по имени)")
    print("3 — delete (удалить контакт)")
    print("4 — list (показать все контакты)")
    print("5 — quit (выход)")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_contact(contacts)

    elif choice == "2":
        search_contact(contacts)

    elif choice == "3":
        delete_contact(contacts)

    elif choice == "4":
        list_contacts(contacts)

    elif choice == "5":
        quit_program()
        break

    else:
        unknown_command()
