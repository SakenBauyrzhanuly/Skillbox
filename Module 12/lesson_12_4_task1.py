# class Unit:
#     def __init__(self, health, damage):
#         self.health = health
#         self.damage = damage
#
#     def __str__(self):
#         return 'Здоровье: {}'.format(self.health)
#
#     def get_damage(self):
#         return self.damage
#
#
# class Solder(Unit):
#     def __init__(self, health, damage):
#         super().__init__(health, damage)
#
#     def get_damage(self):
#         return self.health - self.damage
#
#     def __str__(self):
#         info = super().__str__()
#         info = '\n'.join(
#             (
#                 info, 'Получает урон {} в однократном размере {}'.format(self.damage, self.get_damage())
#             )
#         )
#         return info
#
#
# class Citizen(Unit):
#     def __init__(self, health, damage):
#         super().__init__(health, damage)
#
#     def get_damage(self):
#         return self.health - self.damage * 2
#
#     def __str__(self):
#         info = super().__str__()
#         info = '\n'.join(
#             (
#                 info, 'Получает урон {} в двухкратном размере {}'.format(self.damage, self.get_damage())
#             )
#         )
#         return info
#
#
# solder = Solder(100, 10)
# citizen = Citizen(100, 10)
#
# print(solder)
# print(citizen)

class Unit:
    def __init__(self, hp):
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    def receive_damage(self, damage):
        self.__hp -= damage


class Soldier(Unit):
    def receive_damage(self, damage):
        super().receive_damage(damage)


class Civilian(Unit):
    def receive_damage(self, damage):
        super().receive_damage(damage * 2)


soldier = Soldier(100)
civilian = Civilian(50)

print(soldier.get_hp()) # 100
print(civilian.get_hp()) # 50

soldier.receive_damage(10)
civilian.receive_damage(10)

print(soldier.get_hp()) # 90
print(civilian.get_hp()) # 30