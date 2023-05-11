class Pet:
    legs = 4
    has_tail = True

    def __str__(self):
        tail = 'да' if self.has_tail else 'нет'
        return 'Всего ног: {legs} \n Хвост присутствует - {has_tail}'.format(
            legs=self.legs,
            has_tail=tail
        )

    def walk(self):
        print('Гуляет')


class Cat(Pet):

    def sound(self):
        print('Мяу!')


class Dog(Pet):

    def sound(self):
        print('Гав!')


class Frog(Pet):

    def sound(self):
        print('Ква!')

    def walk(self):
        print('Плавает')

cat = Cat()
dog = Dog()
frog = Frog()
print(cat)
print(dog)

cat.sound()
dog.sound()

cat.walk()
dog.walk()
frog.walk()