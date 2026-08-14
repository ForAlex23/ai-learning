contacts = []

while True:
    print("1 — add (добавить контакт)")
    print("2 — find (найти по имени)")
    print("3 — delete (удалить контакт)")
    print("4 — list (показать все контакты)")
    print("5 — quit (выход)")

    choice = input("Выберите действие: ")

    if choice == "1":
        print("Добавление контакта")

        name = input("Введите имя: ")
        phone = input("Введите номер телефона: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)

    elif choice == "2":
        print("Поиск контакта по имени")
        search_name = input("Введите имя: ").lower()
        found = False
        for contact in contacts:
            if search_name in contact['name'].lower():
                print(f"{contact['name']} - {contact['phone']}")
                found = True
        if not found:
            print("Контакт не найден.")

    elif choice == "3":
        print("Удаление контакта")
        delete_name = input("Введите имя: ").lower()
        found = False
        for contact in contacts:
            if delete_name == contact['name'].lower():
                contacts.remove(contact)
                found = True
        if not found:
            print("Контакт не найден.")
        else:
            print("Контакт удален.")

    elif choice == "4":     
        print("Список всех контактов")
        for contact in contacts:
            print(f"{contact['name']} - {contact['phone']}")

    elif choice == "5":
        print("Выход из программы.")
        break

    else:
        print("Неизвестная команда.")