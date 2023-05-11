
class Toyota:
    color_car = 'Red'
    price_car = 'one million'
    max_speed = 200
    current_speed = 0

    def info(self):
        print(
            'Color car: {}\nPrice a car: {}\nMaximum speed car: {}\nCurrent speed car: {}\n'.format(
                self.color_car, self.price_car, self.max_speed, self.current_speed
            )
        )
    def edit_current_speed(self, new_speed):
        self.current_speed = new_speed
        print('Текущая скорость: {}'.format(new_speed))


my_car = Toyota()
my_car.info()
my_car.edit_current_speed(180)
