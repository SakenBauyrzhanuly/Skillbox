def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('Введите текст:').lower()
hist = histogram(text)
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

my_list = []
for i_m in sorted(hist.values()):
    my_list.append(i_m)

res = []
[res.append(x) for x in my_list if x not in res]
for r in res:
    list_m = [i_list for i_list in hist.keys() if hist[i_list] == r]
    print(r, ':', list_m)

