goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i_store in store.values():
    keyy = {i for i in store if store[i] == i_store}
    ky = str(keyy)
    ky = ky[2:]
    ky = ky[:-2]
    res_key = {i for i in goods if goods[i] == ky}
    res_key = str(res_key)
    res_key = res_key[2:]
    res_key = res_key[:-2]
    summ_res = 0
    summ_store = 0
    for i in i_store:
        result_store = i['quantity'] * i['price']
        summ_store += i['quantity']
        summ_res += result_store
    print(res_key, ' - ', summ_store,'стоимость ',summ_res,'рублей')
