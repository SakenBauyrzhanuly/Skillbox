
contact_dict = dict()
while True:
    name = input('Введите имя: ')
    last_name = input('Введите Фамилию: ')
    fio = (name, last_name)
    if fio not in contact_dict:
        contact_dict[fio] = int(input('Введите номер тел: '))
    else:
        print('Такой контакт уже есть!')
    print(contact_dict)

