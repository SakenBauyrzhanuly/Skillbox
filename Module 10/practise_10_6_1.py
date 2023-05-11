# names_file = open('people.txt', 'r', encoding='utf')
# print('Содержимое файла people.txt: ')
# sum_all_sym = 0
# line_count = 0
# vv = 0
# try:
#     for i_line in names_file:
#         line_count += 1
#         for i_sym in i_line:
#             length = len(i_line)
#             if i_line.endswith('\n'):
#                 length -= 1
#             if length < 3:
#                 vv = line_count
#                 raise Exception('Длина {} строки меньше трех символов'.format(line_count))
#             sum_all_sym += 1
#         print(i_line)
# finally:
#     print('Ошибка: менее трёх символов в строке ', vv)
#     print('Общее количество символов: ', sum_all_sym - vv)

names_file = open('people.txt', 'r', encoding='utf')
print('Содержимое файла people.txt: ')
sum_all_sym = 0
line_count = 0

try:
    for i_line in names_file:
        line_count += 1
        length = len(i_line.strip())  # удаляем пробельные символы с конца и начала строки
        if length < 3:
            raise Exception('Длина {} строки меньше трех символов'.format(line_count))
        sum_all_sym += length
        print(i_line.strip())

except Exception as e:
    print('Ошибка: ', e)

finally:
    names_file.close()
    print('Общее количество символов: ', sum_all_sym)