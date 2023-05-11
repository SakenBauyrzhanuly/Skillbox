from functools import reduce

from typing import List

sentences = ["Nory was a Catholic", "because her mother was a Catholic",
             "and Nory’s mother was a Catholic", "because her father was a Catholic",
             "and her father was a Catholic", "because his mother was a Catholic",
             "or had been"]
# words = [word.lower() for my_str in sentences for word in my_str.split()]
#
# count = reduce(lambda counter, word: counter + 1 if word == 'was' else counter, words, 0)
# print(count)

def check_was(a, b):
    if isinstance(a, str):  # обработаем первый элемент отдельно
        a = int(a.count('was'))
    result = a + int(b.count('was'))
    return result  # т.к. мы возвращаем int - то дальше 'a' всегда будет int-ом, а в 'b' будет новая строка


print(reduce(check_was, sentences))