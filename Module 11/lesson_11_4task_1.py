
class Toyota:

    def __init__(self, color_car, price_car, max_speed, current_speed):
        self.color_car = color_car
        self.price_car = price_car
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print(
            'Color car: {}\nPrice a car: {}\nMaximum speed car: {}\nCurrent speed car: {}\n'.format(
                self.color_car, self.price_car, self.max_speed, self.current_speed
            )
        )

    def edit_current_speed(self, new_speed):
        self.current_speed = new_speed
        print('Текущая скорость: {}'.format(new_speed))


my_car = Toyota('Black', 1000000, 360, 210)
my_car.info()
my_car.edit_current_speed(180)
