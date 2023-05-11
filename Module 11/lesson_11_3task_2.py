class Family:
    name = 'MyFamily'
    money = 100000
    is_home = False

    def family_info(self):
        print(
            'Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
                self.name, self.money, self.is_home
            )
        )

    def earn_money(self, entrance):
        self.money += entrance
        print(
            'Earned {} money! Current value: {}'.format(
                entrance, self.money
            )
        )



    def try_to_buy(self, price_house, discount=0):
        price_house -= price_house * discount / 100
        if self.money >= price_house:
            self.money -= price_house
            self.is_home = True
            print('House purchased! Current money: {}\n'.format(self.money))
        else:
            print('Not enough money\n')



my_family = Family()
my_family.family_info()
print('Try to buy a house')
my_family.try_to_buy(800000)


if not my_family.is_home:
    my_family.earn_money(600000)
    print('Try to buy a house again')
    my_family.try_to_buy(500000, 10)

my_family.family_info()
