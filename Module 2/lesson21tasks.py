# print('Задача 1. Таблица степеней')
#
# numbers = [3,7,5]
# while True:
#
#  number = int(input('Новое число: '))
#
#  numbers.append(number)
#
#  print('Текущий список чисел:', numbers)
#
#  for i in numbers:
#
#    print(i ** 2, i ** 3, i ** 4)
#
#  print()

# print('Задача 2. Очень простая задача')
# numbers = []
# for number in range(100):
#     numbers.append(number)
# print(numbers)

print('Задача 3. Контроль')
numbers = []
count = int(input('Кол-во сотрудников в офисе: '))
for number in range(count):
    number = int(input('ID сотрудника: '))
    numbers.append(number)
print(numbers)
choice = int(input('Какой ID ищем? '))
if choice in numbers:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')
