count_worker = int(input('Количество сотрудников: '))
count = 0
work_list = []
for i in range(count_worker):
    count += 1
    print('Зарплата ',count,'сотрудника: ')
    worker = int(input(''))
    work_list.append(worker)
work_list.remove(0)
print(len(work_list))
print(work_list)


