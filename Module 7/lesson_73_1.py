# my_str = 'so~mec~od~e'
# symbol = '"[@_!#$%^&*()<>?}{~:]"'
# for i_index, i_letter in enumerate(my_str):
#     if i_letter in symbol:
#         print(i_index, end = ' ')


import  random
def get_indexes(where_to_search, what_to_search):
    return [str(index) for index, letter in enumerate(where_to_search) if letter == what_to_search]


text = input("Введите текст: ")
print("Ответ:", " ".join(get_indexes(text, "~")))