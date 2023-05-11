class Robot:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return 'Модель робота: {}'.format(
            self.model
        )


class VacRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.model = model
        self.rubbish_bag = 0

    def operate(self):
        self.rubbish_bag += 10
        print('Текущая заполняемость: {}'.format(self.rubbish_bag))


class WarRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(gun)
        self.model = model
        self.gun = gun

    def operate(self):
        print('Защищается объект с помощью оружия: {}'.format(self.gun))


class WaterRobot(Robot):
    def __init__(self, model, secure_in):
        super().__init__(secure_in)
        self.model = model
        self.secure_in = secure_in

    def operate(self):
        print('Защищается объект под водой с помощью оружия: {}'.format(self.secure_in))


vacrobot = VacRobot('Робот Пылесос')
print(vacrobot)
print(vacrobot.operate())

warrobot = WarRobot('Военный робот', 'Пушка')
print(warrobot)
print(warrobot.operate())

waterrobot = WaterRobot('Подводный Робот', 'Лазер')
print(waterrobot)
print(waterrobot.operate())