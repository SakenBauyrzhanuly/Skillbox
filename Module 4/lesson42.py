# squares = []
# for x in range(10):
#     squares.append(x ** 2)
# squares = [x ** 2 for x in range(10)]
# 
# print(squares)

def get_higher_price(percent, price):
    return round(price * (1 + percent / 100), 2)


prices_now = [1.09, 23.56, 57.84, 4.56, 6.78]
first_percent = int(input('Повышение на первый год:'))
second_percent = int(input('Повышение на второй год:'))
prices_first = [get_higher_price(first_percent, i_price) for i_price in prices_now]
prices_second = [get_higher_price(second_percent, i_price) for i_price in prices_first]

print(prices_first)
print(prices_second)
print('Сумма цен на каждый год:', round(sum(prices_now)), round(sum(prices_first)), round(sum(prices_second)))