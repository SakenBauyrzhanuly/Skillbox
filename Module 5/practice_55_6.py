my_str = 'aaAAbbсaaaA'

init = ''
cntr = 1
curr_str = ''
my_list = []

for i in my_str:
    if init != i:
        my_list.append(curr_str)
        cntr = 1
    elif init == i:
        cntr += 1

    init = i
    curr_str = init + str(cntr)

my_list.append(curr_str)

my_list.remove('')

new_str = ''
for i in my_list:
    new_str += i

print(new_str)