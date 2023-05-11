
# nums_sum = 0
#
# input_data = input('Введите строку: ')
# try:
#     numbers_file_2 = open('numbers3.txt', 'w', encoding='utf-8')
#     if input_data.isnumeric():
#         input_data = int(input_data)
#     numbers_file_2.write(input_data)
#     numbers_file_2.close()
# except FileNotFoundError:
#     print('Такого файла не существет')
# except ValueError:
#     print('Нельзя преобразовать данные в целое.')
# except (PermissionError, FileExistsError):
#     print('Поймано исключение')
# except TypeError:
#     print('Нельзя преобразовать данные в целое.')
# finally:
#     print('программа без ошибок выполнилась')




import os

file = None
try:
    file = open("23.3.txt", "w", encoding="utf8")
    number = int(input("Введите текст: "))
    file.write(str(number))
except (FileNotFoundError, PermissionError) as exc:
    print(type(exc), exc)
except ValueError as exc:
    print(type(exc), exc)
except Exception as exc:
    print(type(exc), exc)
else:
    print("Запись прошла без ошибок")
finally:
    if file and not file.closed:
        file.close()