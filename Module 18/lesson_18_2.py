import re # regular expressions (регулярные выражения)

text = 'AV - Analytics Vidhya AV'

result = re.match(r'AV', text) #поиск в начале строки по шаблону
print('Поиск в начале строки по шаблону: ', result)

print(result.group(0))
print(result.start())
print(result.end())

result = re.match(r'Analytics', text)
print(result)


print('=' * 40)

result = re.search(r'Analytics', text) #поиск  строкe по шаблону
print('поиск  строкe по шаблону: ', result)
print(result.group(0))
print(result.start())
print(result.end())

print('=' * 40)


result = re.findall(r'AV', text) #Все совпадения по шаблон
print('Все совпадения по шаблону: ', result)

print('=' * 40)

text_2 = 'AV - Analytics community of India. India!'

result = re.sub(r'India', 'the World', text_2) #Замена всех найденных шаблонов
print('Замена всех найденных шаблонов: ', result)

print('=' * 40)

pattern = re.compile('AV')
result = pattern.findall(text)
print(result)

result2 = pattern.findall(text_2)
print(result2)