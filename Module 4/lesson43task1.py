import random

num_1 = int(input(' Введите диапазон А: '))
num_2 = int(input(' Введите диапазон Б: '))

list_even = [i for i in range(num_1, num_2) if i % 2 != 0]

print(list_even)