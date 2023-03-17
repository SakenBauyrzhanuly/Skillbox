goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

text = input('Новый фрукт: ')
price = int(input('Цена: '))

new_good = [text, price]
goods.append(new_good)

for el in range(len(goods)):
    goods[el][1] = goods[el][1] * 1.08

print(goods)