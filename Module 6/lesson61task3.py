phone_dict = {}
while True:
    print('Текущие контакты на телефоне')
    if phone_dict:
        for i_name in phone_dict:
            print(i_name,phone_dict[i_name])
    else:
        print('Пусто')
    name = input('Введите имя: ')
    number_phone = int(input('Введите номер телефона: '))
    if name in phone_dict:
        print('Ошибка. Такое им существует')
    else:
        phone_dict[name] = number_phone