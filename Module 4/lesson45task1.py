text = 'Нужно отнести кольцо в Мордор!'
vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

result = [i for i in text if i in vowel]
print('Список гласных букв: ',result)
print('Длина списка: ',len(result))