# phonebook_dict = {
#     'Ваня': 880066565696,
#     'Петя': 870336565693,
#     'Лена': 899566565697,
# }
# name = input('Введите имя: ')
# if name in phonebook_dict:
#     print(phonebook_dict[name])
# else:
#     print('Ошибка: Челвоек с именем {0} не найден'.format(name))

print('--------------')
student_str = input(
    'Введите информацию о студенте через пробел\n'
    '(имя, фамилия, город, место учебы, оценки):'
)
student_info = student_str.split()
student = dict()
student['Имя'] = student_info[0]
student['Фамилия'] = student_info[1]
student['Город'] = student_info[2]
student['Место учебы'] = student_info[3]
student['Оценки'] =[]

for i_grade  in student_info[4:]:
    student['Оценки'].append(int(i_grade))

for i_info in student:
    print(i_info, '-', student[i_info])

print(student)
