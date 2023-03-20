# squares = []
# for x in range(10):
#     if x % 2 != 0:
#         squares.append(x ** 2)
#
#

# squares_odds = [x ** 2 for x in range(10) if x % 2 != 0]
# squares_cubes = [(x ** 2 if x % 2 != 0 else x ** 3) for x in range(10) ]
#
# print(squares_odds)
# print(squares_cubes)


print('Отряды ')
import random

fst_squad = [random.randint(50,80) for _ in range(10)]
scnd_squad = [random.randint(30,60) for _ in range(10)]

thrd_squad_cond = [('Погиб ' if fst_squad[i_damage] + scnd_squad[i_damage] > 100
                    else 'Выжил')
                   for i_damage in range(10)]

print(fst_squad)
print(scnd_squad)
print(thrd_squad_cond)