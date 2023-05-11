nums_sum = 0
nums_count = 0
try:
    numbers_file = open('numbers3.txt', 'r')
    for i_line in numbers_file:
        nums_count += 1
        nums_sum += int(i_line)
    numbers_file.close()
    print('Ариф среднее: ', nums_sum / nums_count)
except FileNotFoundError:
    print('Такого файла не существует')
# except ValueError:
#     print('Нельзя преобразовать данные в целое число!')