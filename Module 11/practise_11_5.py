import random


class Human:
    def __init__(self, name, degree_fullness, home):
        self.name = name
        self.degree_fullness = degree_fullness
        self.home = home

    def eat_food(self):
        degree_fullness = self.degree_fullness + 10
        refrator = self.home.refrator - 10
        print('Нужно поесть')
        return degree_fullness, refrator

    def work(self):
        degree_fullness = self.degree_fullness - 10
        safe_money = self.home.safe_money + 10
        print('Нужно поработать')
        return degree_fullness, safe_money

    def play(self):
        degree_fullness = self.degree_fullness - 10
        print('Нужно поиграть')
        return degree_fullness

    def go_shop(self):
        refrator = self.home.refrator + 10
        safe_money = self.home.safe_money - 10
        print('Нужно шопиться')
        return refrator, safe_money

    def have_a_day(self):
        pass


class Home:
    def __init__(self):
        self.refrator = 50
        self.safe_money = 0


human_first = Human('Tom', 30, Home())
human_second = Human('Jerry', 18, Home())
degree_hum_1 = human_first.degree_fullness
degree_hum_2 = human_second.degree_fullness
for day in range(365):
    gen_cub = [random.randint(1, 6)]
    if degree_hum_1 < 20 or degree_hum_2 < 20:
        degree_hum_1, human_first.refrator = human_first.eat_food()
        degree_hum_2, human_second.refrator = human_second.eat_food()
    elif human_first.refrator < 10 or human_second.degree_fullness < 10:
        human_first.refrator, human_first.safe_money = human_first.go_shop()
    elif human_first.home.safe_money < 50 or human_second.home.safe_money:
        degree_hum_1, human_first.home.safe_money = human_first.work()
        degree_hum_2, human_second.home.safe_money = human_second.work()
    elif gen_cub == 1:
        degree_hum_1, human_first.home.safe_money = human_first.work()
        degree_hum_2, human_second.home.safe_money = human_second.work()
    elif gen_cub == 2:
        degree_hum_1, human_first.refrator = human_first.eat_food()
        degree_hum_2, human_second.refrator = human_second.eat_food()
    else:
        degree_hum_1 = human_first.play()
        degree_hum_2 = human_second.play()
    print('Деньги в сейфе: ', human_first.home.safe_money)
    print('Холодильник с едой: ', human_first.home.refrator)
    print('Сытость {} :'.format(human_first.name), human_first.degree_fullness)
    print('Сытость {} :'.format(human_second.name), human_second.degree_fullness, '\n\n\n')









