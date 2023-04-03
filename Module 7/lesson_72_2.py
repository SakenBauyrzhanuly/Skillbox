def side_full(rad_num, height_num):
    p = 3.14
    side = 2 * p * rad_num * height_num
    S = p * (rad_num ** 2)
    full = side + 2 * S

    return str(side), str(full)


radius = int(input('Введите радиус: '))
height = int(input('Введите высоту: '))

print(side_full(radius, height))
