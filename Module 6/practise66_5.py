

sinonym = dict([input('Введите пару:').split(' - ') for _ in range(3)])
print(sinonym)


while True:
    choice = input('Введите слово: ')
    if choice in sinonym.values():
        for key, value in sinonym.items():
            if choice == value:
                print(key)
    elif choice in sinonym.keys():
        print(sinonym[choice])

    elif choice == 'stop':
        break
    else:
        print('Такого слова в словаре нет')



#
# Введите пару: Привет - Здравствуйте
# {'first': 'Привет', 'second': 'Здравствуйте'}
# Введите пару: Печально - Грустно
# {'first': 'Печально', 'second': 'Грустно'}
# Введите пару: Весело - Радостно
# {'first': 'Весело', 'second': 'Радостно'}