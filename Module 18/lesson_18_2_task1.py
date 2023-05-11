import re

text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'

result = re.match(r'wo', text) #поиск в начале строки по шаблону
print('Поиск в начале строки по шаблону: ', result)

result = re.search(r'wo', text) #поиск  строкe по шаблону
print('Поиск первого найденного совпадения по шаблону: ', result)

print('Содержимое найденной подстроки: ', result.group(0))

print('Начальная позиция: ', result.start())
print('Конечная позиция: ', result.end())

result = re.findall(r'wo', text) #Все совпадения по шаблон
print('Список всех упоминаний шаблона: ', result)

result = re.sub(r'wo', 'ЗАМЕНА', text) #Замена всех найденных шаблонов
print('Замена всех найденных шаблонов: ', result)