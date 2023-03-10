# scores = [8, 5, 10, 7, 6]
# print(scores)
#
# scores[2] *= 3
# x = scores[4]
# x += 10
#
# print(x)
# print(scores)

print('Монстры уроны')

monsters_count = int(input('Количество монстров: '))
mage_index = int(input('Номер мага в списке: '))
monsters_damage = []

for monster in range(monsters_count):
    print('Урон у', monster + 1,'монстра:', end = ' ')
    damage = int(input())
    monsters_damage.append(damage)

for i_monster in range(monsters_count):
    if monsters_damage[i_monster] < 100 and i_monster != mage_index - 1:
        monsters_damage[i_monster] += monsters_damage[mage_index - 1]



print('Итоговый урон монстра: ', monsters_damage)