# number_list = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
#
# f_el = number_list[0]
# l_el = number_list[-1]
#
# number_list.pop(0)
# number_list.pop(-1)
#
# number_list.insert(0, l_el)
# number_list.append(f_el)
#
# print(number_list)

number_list = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]

# printing the original list
print("Изначальный список:  ", number_list)

# Shift from Front to Rear in List using a loop and temporary variable
temp = number_list[0]
for i in range(len(number_list) - 2):
    number_list[i] = number_list[i + 2]
number_list[-2] = temp

print("Сдвинутый список: ", number_list)