class Property:
    def __init__(self, price):
        self.price = price

    def tax_method(self, tax):
        result = self.price / tax
        return result


class Apartment(Property):
    def tax_method(self, tax):
        return super().tax_method(tax)


class Car(Property):
    def tax_method(self, tax):
        return super().tax_method(tax)


class CountryHouse(Property):
    def tax_method(self, tax):
        return super().tax_method(tax)


def main():
    price_property = int(input('Введите стоимость имущества: '))

    apartment = Apartment(price_property)
    print(apartment.tax_method(1000))
    car = Car(price_property)
    print(car.tax_method(500))
    house = CountryHouse(price_property)
    print(house.tax_method(200))
    case_money = int(input('Введите деньги на счету : '))
    if apartment.tax_method(1000) + car.tax_method(500) + house.tax_method(200) < case_money:
        print(case_money - (apartment.tax_method(1000) + car.tax_method(500) + house.tax_method(200)))
    else:
        print('Не хватает суммы: ', case_money - (apartment.tax_method(1000) + car.tax_method(500) + house.tax_method(200)))


main()

# В этом коде мы создали базовый класс Property, от которого наследуются классы Apartment, Car и CountryHouse.
# Каждый из дочерних классов имеет свой конструктор, который вызывает конструктор базового класса, передавая ему стоимость имущества.
#
# Также каждый из дочерних классов переопределяет метод calculate_tax(),
# который возвращает налог на соответствующее имущество, вычисленный по заданным формулам.
#
# В функции main() мы запрашиваем у пользователя количество денег и стоимость имущества, создаем объекты каждого из дочерних классов,
# вычисляем налог на каждое из них и выводим результаты на экран. После этого проверяем, хватает ли у пользователя денег на оплату налогов.
# Если нет, то выводим соответствующее сообщение.
# Если да, то выводим, сколько денег останется после оплаты налогов.