# class CanFly:
#     def __init__(self, height, speed):
#         self.height = height
#         self.speed = speed
#
#     def take_off(self):
#         return self.height
#
#     def fly(self):
#         return self.speed
#
#     def land_to(self):
#         pass
#
#     def info_h_s(self):
#         return 'Высота {} и скорость {}\n'.format(self.height, self.speed)
#
#
#
#
#
# class ButterFly(CanFly):
#     pass
#
#
# class Rocket(CanFly):
#
#     def land_to(self):
#         self.height=0
#         print('Ракета может при выcоте {} взрываться'.format(self.height))
#
# butterfly = ButterFly(1, 0.5)
# print(butterfly.info_h_s())
#
# rocket = Rocket(500, 1000)
# print(rocket.info_h_s())
# print(rocket.land_to())



class CanFly:

    def __init__(self):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        pass

    def fly(self):
        pass

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def __str__(self):
        return '{} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class Butterfly(CanFly):

    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.1


class Aircraft(CanFly):

    def take_off(self):
        self.velocity = 300
        self.altitude = 1000

    def fly(self):
        self.velocity = 800


class Missile(CanFly):

    def take_off(self):
        self.velocity = 1000
        self.altitude = 10000

    def land_on(self):
        self.altitude = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print('Ракета показала себя великолепно. Только упала не на ту планету (C) Вернер фон Браун')