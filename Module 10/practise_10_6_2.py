import random

number = 0
nums = 0
while nums <= 777:
    num = (random.randint(1, 13))
    print('Число исключения: ', num)
    if num == 7:
        raise Exception('Вас постигла неудача!')
    number = int(input('Введите число: '))
    with open('out_file.txt', 'a') as number_file:
        number_file.write(str(number) + '\n')
        nums += number

print(number)
