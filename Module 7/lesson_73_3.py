def encount_prog(db_d):
        result = []
        if isinstance(db_d, dict):
            db_d = db_d.values()
        for i_index, i_let in enumerate(db_d):
            if i_index % 2 == 0:
                result.append(i_let)
        return result







my_str = 'О Дивный Новый мир!'
print(encount_prog(my_str))

my_list = [100, 200, 300, 'буква', 0, 2, 'а']
print(encount_prog(my_list))

print(encount_prog({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))