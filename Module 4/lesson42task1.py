first_side = int(input('Левая граница: '))
second_side = int(input('Правая граница: '))

cube = [i ** 3 for i in range(first_side, second_side)]
quadrate = [i ** 2 for i in range(first_side, second_side)]
print('Список кубов чисел в диапазоне от ',first_side,'до',second_side,':',cube)
print('Список квадратов чисел в диапазоне от ',first_side,'до',second_side,':',quadrate)