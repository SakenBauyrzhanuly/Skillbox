import random
import string
# my_dict_1 = {}
# my_dict_2 = {}
# my_list_1 = [random.choice(string.ascii_letters) for x in range(10)]
# my_list_2 = [random.choice(string.ascii_letters) for x in range(10)]
# print(my_list_1)
# print(my_list_2)
# for i_index, i_list in enumerate(my_list_1):
#     my_dict_1[i_index] = i_list
# print(my_dict_1)
# for i_index_2, i_list_2 in enumerate(my_list_2):
#     my_dict_2[i_index_2] = i_list_2
# print(my_dict_2)
#
#


def get_random_letter(n):
    return random.choices([chr(i) for i in range(ord("а"), ord("я"))], k=n)

first_list = get_random_letter(10)
second_list = get_random_letter(10)

first_dict = dict(enumerate(first_list))
second_dict = dict(enumerate(second_list))

print(first_dict)
print(second_dict)