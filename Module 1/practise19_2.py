def sumNum(N):
    summa = 0
    while N != 0:
        last_num = N % 10
        summa += last_num
        N //= 10
    print(('\n Итоговая сумма цифр: ', summa))
    return summa

def colNum(numb):
    count = 0
    while numb != 0:
        count += 1
        numb //= 10
    print(('\n Количество цифр: ', count))
    return count

num = int(input('Введите число: '))
sumNum(num)
colNum(num)
sum = sumNum(num)
count = colNum(num)
print('Разность суммы и количества цифр: ', sum - count)