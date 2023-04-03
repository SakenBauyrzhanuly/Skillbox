x = ['example.txt']

prefix = ('@', '#', '*', '&')
postfix = ('.txt', '.doc')
for item in x:
    if item.startswith(prefix) == False and item.endswith(postfix):
        print('Файл назван верно.', item)
    elif item.startswith(prefix) == False:
        print('Ошибка: название начинается недопустимым символом', item)
    elif item.endswith(postfix) == False:
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.',item)