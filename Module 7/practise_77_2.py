def isPrime(num):
    if num < 2:  # числа меньше двух не являются простыми
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # если число делится на какое-то число из диапазона от 2 до корня из числа, то оно не является простым
            return False
    return True
def crypto(my_list):
    result_crypt = [letter  for index, letter in enumerate(my_list) if isPrime(index)]
    return result_crypt





print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))