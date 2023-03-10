# print('Задача 1. Гугл')
# nums_list = []
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#     nums_list.append(num)
#
# maximum = 0
# minimum = -1
#
# for i in nums_list:
#     if maximum < i:
#         maximum = i
#
#     if minimum > i:
#         minimum = i
#
# print('Максимальное число в списке:', maximum)
#
# print('Минимальное число в списке:', minimum)

# print('Задача 2. Кратность')
#
# N = int(input('Кол-во чисел в списке: '))
# nums_list = []
# count = 0
# for j in range(N):
#     count += 1
#     num = int(input(f'Введите {j} число:  '))
#     nums_list.append(num)
# print(nums_list)
# divider = int(input('Введите делитель: '))
# summ = 0
# for i in nums_list:
#     if i % divider == 0:
#         i //= 10
#         summ += i
# print('Сумма индексов: ',summ)

print('Задача 3. Собачьи бега')

nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

if nums_list:
    maximum = nums_list[0]
    minimum = nums_list[0]

    minimum_index = 0
    maximum_index = 0
    for index, i in enumerate(nums_list):

        if maximum < i:
            maximum = i
            maximum_index = index

        if minimum > i:
            minimum = i
            minimum_index = index

    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)

    print(nums_list)
    nums_list[minimum_index], nums_list[maximum_index] = nums_list[maximum_index], nums_list[minimum_index]
    print(nums_list)
else:
    print('В списке нету чисел')
