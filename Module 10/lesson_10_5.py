sym_sum = 0
line_count = 0
try:
    with open('people.txt', 'r') as people_file:
        for i_line in people_file:
            length = len(i_line)
            line_count += 1
            if i_line.endswith('\n'):
                length -= 1
            if length < 3:
                raise BaseException('Длина {} строки меньше трех символов'.format(line_count))
            sym_sum += length
except FileNotFoundError:
    print('Файл не найден')
finally:
    print('Найденная сумма символов: ', sym_sum)
    print(people_file.closed)