user_name = input('Введите Имя: ')
file_name = input('Введите долг: ')

order = '{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}!'.format(user_name, file_name)

print(order)