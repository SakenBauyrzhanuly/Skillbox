# word = input('Введите слово: ')
# replace_num = int(input('Номер символа для замены: '))
# replace_sym = input('Чем заменяем: ')
#
# sym_list = []
# for sym in  word:
#     sym_list.append(sym)
#
# sym_list[replace_num - 1] = replace_sym
#
# for i in sym_list:
#     print(i, end = ' ')


words_list = []
counts = [0, 0, 0]

for i in range(3):
    print('Введите ', i + 1,'слово: ', end = ' ')
    word = input()
    words_list.append(word)

text = input('Слово из текста: ')
while text != 'end':
    for index in range(3):
        if words_list[index] == text:
            counts[index] += 1
    text = input('Слово из текста: ')
print('Подсчет слов в тексте ')
for i in range(3):
    print(words_list[i],':',counts[i])