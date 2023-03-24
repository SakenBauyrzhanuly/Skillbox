user_name = input('Введите пользователя: ')
file_name = input('Введите имя файла: ')
path = 'C:/{user}/docs/folder/{new_file}.txt'.format(
    user = user_name,
    new_file = file_name)


path_2 = 'C:/{0}/docs/{0}/folder/{1}.txt'.format(
    user_name,
    file_name)

path_3 = f'C:/{user_name}/docs/folder/{file_name}.txt'


print('Путь к файлу: ', path)
print('Путь к файлу: ', path_2)
print('Путь к файлу: ', path_3)


print('-------------------')

# while True:
#     grats_template = input('Введите шаблон поздравления, '
#                        'в шаблоне нужно использовать конструкцию {name}: ')
#     if '{name}' in grats_template:
#         break
#     print('Ошибка: отсутствует конструкция {name}.')
#
# print('Введите список имен (заканчивается на end): ')
# name_list = []
# while True:
#     name = input('Имя: ')
#     if name != 'end':
#         name_list.append(name)
#     else:
#         break
# for i_name in name_list:
#     print(grats_template.format(name = i_name))
