array_1 = [1, 5, 10, 20, 40, 80, 100]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
array_1_s = set(array_1)
array_2_s = set(array_2)
array_3_s = set(array_3)


print('Задача 1. Решение с множеств: ', array_1_s.intersection(array_2_s).intersection(array_3_s))
print('Задача 2. Решение с множеств: ', array_1_s.difference(array_2_s).difference(array_3_s))
result_1 = []
for i in array_1:
    if i in array_2 and i in array_3:
        result_1.append(i)
print('Задача 1. Решение без множеств: ', result_1)

result_2 = []
for i in array_1:
    if i not in array_2 and i not in array_3:
        result_2.append(i)
print('Задача 2. Решение без множеств: ',result_2)