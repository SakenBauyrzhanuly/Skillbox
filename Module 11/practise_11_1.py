import random


class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 20

    def get_damage(self, dmg):
        self.health -= dmg

    def print_info_hp(self):
        print('У война {} Осталось {} hp\n'.format(self.name, self.health))

    # def damage_random(self, random_choice):
    #     random_choice = random.randint(1, 2)
    #     return random_choice


war_1 = Warrior('Spider_Man')
war_2 = Warrior('Bat_Man')

print(war_1.name, war_1.health, war_1.damage)
print(war_2.name, war_2.health, war_2.damage)
while True:
    if war_1.health == 0 or war_2.health == 0:
        pass
        if war_1.health > war_2.health:
            print('Побеждает {}'.format(war_1.name))
        else:
            print('Побеждает {}'.format(war_2.name))
        break
    rand_dam = random.randint(1, 2)
    if rand_dam == 1:
        war_2.get_damage(war_1.damage)
        war_1.print_info_hp()
        war_2.print_info_hp()
    elif rand_dam == 2:
        war_1.get_damage(war_2.damage)
        war_1.print_info_hp()
        war_2.print_info_hp()

