class Ship:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return 'Модель корабля: {}'.format(
            self.model
        )


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.model = model
        self.gun = gun

    def attack(self):
        print('Корбаль атакует с помощью оружия: {}'.format(
            self.gun
        ))




class CargoShip(Ship):
    pass


warship = WarShip('Qwer45', 'Пулемет')
print(warship)
warship.attack()