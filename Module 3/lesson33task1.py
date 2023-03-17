main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]
main.extend(first_company)
second_company.extend(third_company)
main.extend(second_company)
k = main.count(0)
print('Общий список задач: ', main)
print('Кол-во невыполненных задач: ',k)