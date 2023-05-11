class Person:
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.__count += 1

    def __str__(self):
        return  'Имя: {} \t Возраст: {}'.format(self.__name, self.__age)

    def get_count(self): #геттер
        return self.__count

    def get_age(self):
        return self.__age

    def set_age(self, age): #сеттер
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недоспустимый возраст')


misha = Person('Misha', 20)
tom = Person('Tom', 25)
print(misha.get_count())
new_age = 80
misha.set_age(new_age)
print(misha.get_age())



# misha.age = new_age


# print(misha)
# Person.__count -= 1
# print(Person.__count)