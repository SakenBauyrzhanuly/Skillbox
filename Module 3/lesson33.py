# print('Interesting films')
# my_list = ['Крепкий орешек', 'Назад в будущее', 'Таксист']
# your_list = [ 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
#
# my_list.extend(your_list)
# my_list.extend('Alladin')
# for i_elem in my_list:
#     print(i_elem)
#


print('Пацеты')
pack = []
decode = []
bad_packs = 0

packs_amt = int(input('Количество пакетов: '))

for i_pack_num in range(packs_amt):
    print('\n Пакет номер ', i_pack_num + 1)
    for i_bit in range(4):
        print(i_bit + 1, 'бит: ', end=' ')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Много ошибок в пакете ')
        bad_packs += 1
    pack = []
print('\n Полученное сообщение: ', decode)
print('Количество ошибок в сообщении: ', decode.count(-1))
print('Количество потерянных пакетов: ', bad_packs)
