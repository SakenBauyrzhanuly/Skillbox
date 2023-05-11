class Monitor:
    name_produce = 'Samsung'
    matrix = 'VA'
    res_display = 'WQHD'
    frequence = 60

class Headphone:
    name_hp = 'Sony'
    sensitivity_hp = 108
    micro_hp = False

monitors = [Monitor() for _ in range(4)]
print(monitors)
headphones = [Headphone() for _ in range(3)]
print(headphones)

for i, j in enumerate([60, 144, 70, 60]):
    monitors[i].frequence = j
    print(monitors[i].frequence)

headphones[0].micro_hp = False