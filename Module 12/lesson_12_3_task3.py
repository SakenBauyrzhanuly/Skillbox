class MyCustomException(Exception):
    pass

# raise MyCustomException('Это моя ошибка!')


class DivisionError(Exception):
    print('нельзя делить меньшее на большее')


numbers_file = open('number_9.txt', 'r', encoding='utf-8')
for i_line in numbers_file:
    try:
        clear_line = i_line.rstrip(' ')
        i_num_1, i_num_2 = clear_line.rsplit()
        if int(i_num_1) < int(i_num_2):
            raise DivisionError
        else:
            res = int(i_num_1) // int(i_num_2)
            print(res)
    except ValueError:
        print('ValueError')

numbers_file.close()

