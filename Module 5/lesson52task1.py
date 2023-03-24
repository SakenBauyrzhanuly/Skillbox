user_name = input('Введите Имя: ')
file_name = input('Введите номер заказа: ')

order = 'Здравствуйте, {user_name}! Ваш номер заказа: {file_name}. Приятного дня!'.format(user_name = user_name, file_name = file_name)

print(order)