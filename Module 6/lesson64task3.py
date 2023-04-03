# text = 'ab1n32kz2'
# set_text = set(text)
# res_text = set()
# for i in set_text:
#     if '0' <= i <= '9':
#         res_text.add(i)
# print(res_text)
#


text = input("Введите строку: ")
text_unique = set(text)
result = text_unique & set("0123456789")
# При помощи множества выделим из строки только общие элементы (цифры) и посчитаем длину множества
print(''.join(result))

# # Решение через цикл и сравнение:
# new_result = set()
# for symbol in text:
#     if '0' <= symbol <= '9':
#         new_result.add(symbol)
#
# print(''.join(new_result))