class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()


class Earth:
    def __str__(self):
        return 'Земля'


class Fire:
    def __str__(self):
        return 'Огонь'


class Storm:
    def __str__(self):
        return 'Шторм'


class Vapor:
    def __str__(self):
        return  'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


water = Water()
air = Air()
fire = Fire()
earth = Earth()
print(air + water, water + fire, water + earth)


