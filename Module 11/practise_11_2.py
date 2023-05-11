import random


class Students:
    def __init__(self, fi, group_number, performance):
        self.fi = fi
        self.group_number = group_number
        self.performance = performance


name_list = ['Иван Иванов', 'Алехеу Игорев',
             'Влад Вдалеа', 'Самат Смаков',
             'Тест Тевсов', 'Арон Атабек',
             'Аренс Лвоа', 'Лев Толстой',
             'Хй Простой', 'Человек Бала']

group_number_list = [random.randint(6, 10) for _ in range(10)]
performance_list = [[random.randint(1, 5) for _ in range(5)] for _ in range(10)]

students = [Students(fi=name_list[index], group_number=group_number_list[index], performance=performance_list[index])
            for index in range(10)]

for item in students:
    ave_per = round(sum(item.performance) / len(item.performance))
    print(item.fi, item.group_number, sorted(ave_per))

