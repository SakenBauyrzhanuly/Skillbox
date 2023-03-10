# print('Задача 1. Текстовый редактор: возвращение')
# word = input('Введите слово: ')
# # res = word.replace(':', ';')
# # print(res)
#
# replace_sym = input('Чем заменяем: ')
# text = ':'
# count = 0
# res = ''
# for i in range(len(word)):
#     if word[i] == text:
#         res = word.replace(word[i], ';')
#         count += 1
#
#
# print('Кол-во замен: ', count)
# print(res)

print('Задача 2. Соседи')
word = input('Введите строку: ')
r_n = int(input('Номер символа: '))

print(word[r_n-1-1], '  ', word[r_n-1+1])

# for i in range(len(word)):


