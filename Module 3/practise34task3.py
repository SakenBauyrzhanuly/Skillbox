shop = [['каретка', 1200], ['шатун', 1000], ['седло1', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input('Название детали: ')
count = int(input('Количество деталей: '))
new_choose = [name,count]
for el in range(len(shop)):
    if shop[el][0] == name:
        summ_price = shop[el][1] * count
print('Общая стоимость: ', summ_price)
