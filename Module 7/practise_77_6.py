#
# contact_dict = dict()
# while True:
#     choice = int(input('Выберите номер действия: \n 1. Добавить контакт \n 2. Найти контакт\n'))
#     if choice == 1:
#         fio = input('Введите имя и фамилию (через пробел): ')
#         fio = tuple(fio.split(' '))
#         if fio not in contact_dict:
#             contact_dict[fio] = int(input('Введите номер тел: '))
#         else:
#             print('Такой контакт уже есть!')
#         print(contact_dict)
#     elif choice == 2:
#         find_info = input('Введите имя или фамилию: ')
#         for k in contact_dict.keys():
#             if find_info in k[0] or find_info in k[1]:
#                 print(k, ' ', contact_dict[k])
#

def add_contact(contacts):
    full_name = tuple(input("Введите имя и фамилию нового контакта (через пробел): ").split())
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
    action = input("Введите номер действия:\n1. Добавить контакт.\n2. Найти человека.\n")
    if action == "1":
        add_contact(contacts)
    elif action == "2":
        find_contact(contacts)
    else:
        print("Неверный номер действия.")
