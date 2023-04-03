data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}
number = int(input('Введите номер паспорта: '))
number_pass = int(input('Введите серию паспорта: '))
for i_pass, j_pass in data.items():
    if (number, number_pass) in (i_pass, j_pass):
        print(data[j_pass])
    else:
        print('В данных отсутствует аналогичные записи!')
    # if (number,number_pass) in data.items():
