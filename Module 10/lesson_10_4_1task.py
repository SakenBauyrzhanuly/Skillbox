names_list = []
line_count = 0
while True:
    try:
        name = input('Введите имя: ')
        for i_line in name:
            length = len(i_line)
            line_count += 1
            if i_line.endswith('\n'):
                length -= 1
            if length < 3:
                raise BaseException('Длина {} строки меньше трех символов'.format(line_count))
    except TypeError:
        print('Ты чего ввел? ')


names_file = open('names.txt', 'w')
names_file.write('\n'.join(names_list))
names_file.close()
print('Программа закончена, запись завершена.')