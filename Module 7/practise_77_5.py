import random



def tpl_sort(my_tpl):
    for item in my_tpl:
        if not isinstance(item, int):
            return my_tpl
    return tuple(sorted(my_tpl))


# tpl = tuple(random.randint(0, 10) for _ in range(10))
tpl = (6, 3, -1, 8, 4, 10, -5)
# tpl = (6, 3, 'a', 8, 4, 10, -5)
print(tpl)
print(tpl_sort(tpl))


# def tpl_sort(tpl):
#     if all(isinstance(i, int) for i in tpl):
#         return tuple(sorted(tpl))
#     else:
#         return tpl