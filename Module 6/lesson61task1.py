# print('--------------')
# student_str = input(
#     'Введите информацию о студенте через пробел\n'
#     '(имя, фамилия, город, место учебы, оценки):'
# )
# student_info = student_str.split()
# student = dict()
# student['Имя'] = student_info[0]
# student['Фамилия'] = student_info[1]
# student['Город'] = student_info[2]
# student['Место учебы'] = student_info[3]
# student['Оценки'] =[]
#
# for i_grade  in student_info[4:]:
#     student['Оценки'].append(int(i_grade))
#
# for i_info in student:
#     print(i_info, '-', student[i_info])
#
# print(student)

number = int(input('Введите целое число: '))
result = {}
for i in range(1,number + 1):
    result[i] = i ** 2
print(result)