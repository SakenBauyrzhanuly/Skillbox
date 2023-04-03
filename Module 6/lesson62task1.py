small_storage = {

    'гвозди': 5000,

    'шурупы': 3040,

    'саморезы': 2000

}
big_storage = {

    'доски': 1000,

    'балки': 150,

    'рейки': 600

}
big_storage.update(small_storage)
print(big_storage)
enter_name = input('Введите наименование: ')
if enter_name in big_storage:
    print(big_storage.get(enter_name))
else:
    print('Ошибка')

