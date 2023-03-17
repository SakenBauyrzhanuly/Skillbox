first_sms = input('Первое сообщение: ')
second_sms = input('Второе сообщение: ')
symbol_1 = ('!')
symbol = ('?')
# result = ''
count_sym_1 = first_sms.count(symbol)
count_sym_2 = first_sms.count(symbol_1)
count_sym_3 = second_sms.count(symbol)
count_sym_4 = second_sms.count(symbol_1)

count_first = count_sym_1 + count_sym_2
count_second = count_sym_3 + count_sym_4

if count_first > count_second:
    result = first_sms + second_sms
else:
    result = second_sms + first_sms
print('Третье сообщение: ', result)
