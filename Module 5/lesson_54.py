# user_name = input('Введите пользователя: ')
# file_name = input('Введите имя файла: ')
# path = 'D:/{user}/docs/folder/{new_file}'.format(
#     user = user_name,
#     new_file = file_name)
#
# if not path.endswith('.txt'):
#     print('ошибка: Неверное расширение файла. ')
# elif not path.startswith('C:/'):
#     print('Ошибка. Неверно указан диск.')
# else:
#     print('Путь к файлу: ', path)

print('---------------------------------------')

words_list = []
for i_num in range(3):
    print('Введите', i_num + 1, 'слово:', end = ' ')
    # word = input().lower()
    word = input().upper()
    words_list.append(word)

# text = input('Введите текст: ').lower().split()
text = input('Введите текст: ').upper().split()

print('Подсчет слов в тексте ')
for index in range(3):
    print(words_list[index], ':', text.count(words_list[index]))