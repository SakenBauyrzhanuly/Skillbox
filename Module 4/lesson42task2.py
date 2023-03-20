str_ent = input('Введите строку: ')
dop_symbol = input('Введите дополнительный символ: ')

len_str = [i * 2 for i in str_ent]
with_symbol = [i + dop_symbol for i in len_str]
print('Список удвоенных символов: ',len_str)
print('Склейка с дополнительным символом: ',with_symbol)




