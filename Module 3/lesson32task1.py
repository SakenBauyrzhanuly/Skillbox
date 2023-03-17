
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1,'bear')
zoo.remove('elephant')
i_zoo_1 =zoo.index('lion')
i_zoo_2 =zoo.index('monkey')

print(zoo)
print('Лев сидит в клетке номер', i_zoo_1 + 1)
print('Обезьяна  сидит в клетке номер', i_zoo_2 + 1)
