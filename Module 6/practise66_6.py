my_dict = {}
count_order = int(input('Введите количество заказов: '))
summ_pizza = 0
for i in range(count_order):
    random_str = input(f"Заказ {i+1}: ").split()
    user_name, order_name, order_count = random_str[0], random_str[1], int(random_str[2])
    if user_name not in my_dict:
        my_dict[user_name] = {}
    if order_name not in my_dict[user_name]:
        my_dict[user_name][order_name] = order_count
    else:
        my_dict[user_name][order_name] += order_count

for user_name in my_dict:
    print(user_name + ":")
    for order_name in (my_dict[user_name]):
        print(order_name + ":", my_dict[user_name][order_name])










# n = int(input("Введите количество заказов: "))
# orders = {}
#
# # заполнение словаря информацией о заказах
# for i in range(n):
#     order = input(f"Заказ {i+1}: ").split()
#     name, pizza, count = order[0], order[1], int(order[2])
#     if name not in orders:
#         orders[name] = {}
#     if pizza not in orders[name]:
#         orders[name][pizza] = count
#     else:
#         orders[name][pizza] += count
#
# # сортировка словаря и вывод информации
# for name in sorted(orders):
#     print(name + ":")
#     for pizza in sorted(orders[name]):
#         print(pizza + ":", orders[name][pizza])
