
class Person:
    """
    Базовый класс описывающий человека
    __count общее количество человек

    Args:
        name(str): передается имя человек
        age(int): передается возраст человек

    Attributes:
        max_count(int):  макисмальное количество инстансов
    """
    __count = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Person.__count += 1

    def __str__(self):
        return  'Имя: {} \t Возраст: {}'.format(self.__name, self.__age)

    def get_count(self): #геттер
        return self.__count

    def get_name(self):
        return self.__name

    def get_age(self):
        """
        Геттер для получения возраста
        :return: __age
        :rtype: int
        """
        return self.__age



    def set_age(self, age): #сеттер
        """
        Сеттер для установления возраста
        :param age: возраст
        :raise Exceptiopn: если возраст не в границах от 1 до 90 то вызывается исключение
        :return:
        """
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception('Недоспустимый возраст')





class Student(Person):
    def __init__(self, name, age, univercity):
        super().__init__(name, age)
        self.univercity = univercity

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Student учится в университете {}'.format(self.univercity)

            )
        )
        return info
        #return  'Student {} учится в университете {}'.format(self.get_name(), self.univercity)

class Employee(Person):
    """
    Класс Работник Родитель: Person
    Args:
        name(str): передается имя человек
        age(int): передается возраст человек
    Attributes:
        max_count(int):  макисмальное количество инстансов
        job (str): Должность работника
    """
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def __str__(self):
        info = super().__str__()
        info = '\n'.join(
            (
                info,
                'Company {}:\t ZP: {}'.format(self.company, self.salary)

            )
        )
        return info


my_student = Student('Tom', 24, 'MGU')
print(my_student)

my_emp = Employee(name='Bob', age=25, salary=10000, company='Company')
print(my_emp)

print(Person.__doc__)


# misha.age = new_age


# print(misha)
# Person.__count -= 1
# print(Person.__count)