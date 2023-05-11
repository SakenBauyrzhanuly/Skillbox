# Эта задача предлагает реализовать класс для представления точки на плоскости с возможностью создания новой точки с пользовательскими координатами
# или с координатами по умолчанию и методом для получения информации о точке.
# Также требуется внутри класса создать счётчик,
# который будет отслеживать количество созданных точек.
#
# Чтобы выполнить задачу, необходимо создать класс с именем "Point" и определить в нем метод init(),
# который будет принимать два аргумента для координат x и y.
# Если аргументы не передаются, координаты
# будут установлены на значение по умолчанию (0,0).
# В методе init также нужно увеличивать счетчик созданных объектов.
#
# Для получения информации о точке можно определить метод с именем "get_info()", который будет возвращать строку с координатами точки.
# В этом методе можно использовать атрибуты объекта, чтобы получить значения координат.
#
# Внутри класса можно создать переменную класса с именем "counter", которая будет увеличиваться при каждом создании нового объекта типа "Point".
# Для доступа к переменной класса используется синтаксис "ClassName.variable_name".


class Point:
    count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.count += 1

    def get_x(self):
        return self.__x

    def set_x_y(self, x, y):
        if isinstance(x, int):
            self.__x = x
        else:
            print("{} не является целым.".format(x))
        if isinstance(y, int):
            self.__y = y
        else:
            print("{} не является целым.".format(y))

    def get_y(self):
        return self.__y

    def __str__(self):
        return "Point({}, {})".format(self.__x, self.__y)


# p_1 = Point()
# new_p = Point(3, 4)
#
# p_1.set_x_y(new_p)
#
# print(p_1.get_x(), p_1.get_y())
# # print(p_2.get_x(), p_2.get_y())
# print(Point.count)
p = Point()
p.set_x_y(8, 9)

print(p.get_x(), p.get_y())