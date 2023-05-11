

def add_contact(contacts):
    full_name = tuple(input("Введите имя и фамилию нового контакта (через пробел): ").strip().split(' '))
    if full_name in contacts:
        print("Такой человек уже есть в контактах.")
    else:
        phone_number = input("Введите номер телефона: ")
        contacts[full_name] = phone_number
        print("Текущий словарь контактов:", contacts)

def find_contact(contacts):
    last_name = input("Введите фамилию для поиска: ").lower()
    found_contacts = []
    for full_name, phone_number in contacts.items():
        if last_name in full_name[1].lower():
            found_contacts.append((full_name, phone_number))
    if found_contacts:
        print("\n".join([f"{full_name[0]} {full_name[1]} {phone_number}" for full_name, phone_number in found_contacts]))
    else:
        print("Контакты с такой фамилией не найдены.")

contacts = {}

while True:
    try:
        action = int(input("Введите номер действия:\n1. Добавить контакт.\n2. Найти человека.\n"))
        if action == int(1):
            add_contact(contacts)
        elif action == int(2):
            find_contact(contacts)
        else:
            print("Неверный номер действия.")
    except ValueError:
            print('Неправильный тип данных')
    else:
        print("Запись прошла без ошибок")

