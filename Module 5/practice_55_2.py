my_str = 'sdcsdcsd dcdc dcdcdcdcdcdcd dc'
my_arr = my_str.split()
my_arr_length = [len(x) for x in my_arr]
max = 0
c_max = 0
for i in range(len(my_arr_length) - 1):
    if my_arr_length[i] > max:
        max = my_arr_length[i]
        c_max = i

print(f'Max word is {my_arr[c_max]} and count is {max}')