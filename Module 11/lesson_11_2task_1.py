import random


class Toyota:
    color_car = 'Red'
    price_car = 'one million'
    max_speed = 200
    current_speed = 0

first_toyota = Toyota()
first_toyota.current_speed = (random.randint(0, 200))

second_toyota = Toyota()
second_toyota.current_speed = (random.randint(0, 200))

third_toyota = Toyota()
third_toyota.current_speed = (random.randint(0, 200))

print(first_toyota.current_speed)
print(second_toyota.current_speed)
print(third_toyota.current_speed)