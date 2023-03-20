original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

res_price = [(num if num > 0 else  '0')
             for num in original_prices]

print(res_price)