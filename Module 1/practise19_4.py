def findCircle(x,y,R):
    if x <= R or y <= R or x == 0 or y == 0:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')




print('Введите координаты монетки:')
x = float(input('x: '))
y = float(input('y: '))
R = float(input('Введите радиус: '))

findCircle(x,y,R)