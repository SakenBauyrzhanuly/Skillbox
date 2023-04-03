
def my_list_func(ip):
    my_list = ip.split('.')
    print(my_list)
    new_list = []
    if len(my_list) != 4:
        return 'Адрес — это четыре числа, разделённые точками.'
    for i in range(len(my_list)):
         if 0 <= int(my_list[i]) <= 255:
            new_list.append(my_list[i])
         else:
            print(my_list[i], '- превышает интервал')


ip = input('Введите IP: ')
result = my_list_func(ip)
print(result)


# def is_valid_ip_address(ip):
#     # Разделяем строку на части, разделённые точками
#     parts = ip.split('.')
#
#     # IP-адрес должен содержать ровно 4 части
#     if len(parts) != 4:
#         return 'Адрес — это четыре числа, разделённые точками.'
#
#     for part in parts:
#         try:
#             # Каждая часть должна быть целым числом в диапазоне от 0 до 255
#             if not 0 <= int(part) <= 255:
#                 return f'{part} превышает 255.'
#         except ValueError:
#             # Если преобразование в целое число не удалось, значит, это не число
#             return f'{part} — это не целое число.'
#
#     return 'IP-адрес корректен.'
#
#
# ip = input('Введите IP: ')
# result = is_valid_ip_address(ip)
# print(result)