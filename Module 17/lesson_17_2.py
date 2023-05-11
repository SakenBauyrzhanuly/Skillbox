def f1():
    print('Внутри f1 num =', number)


def f2():
    number = 50  # локальная переменная
    print('Внутри f2 num =', number)


def f3():
    def f4():
        # global number
        nonlocal number
        number = 10
        print('Внутри f3/f4 num =', number)

    number = 30
    print('Внутри f3 num =', number)
    f4()
    print('Внутри f4 num =', number)


number = 100  # глобальное переменное
print('global num =', number)
f1()
f2()
f3()
print('global num =', number)
