def add_num(seq, number):
    seq = list(seq)
    for i_num in range(len(seq)):
        seq[i_num] += number
    return seq

origin_tuple = (3, 1, 4, 1, 5)
changed_list = add_num(origin_tuple, 5)

print(origin_tuple)
print(changed_list)



# nums = (10, 20, 30, 40)
# nums[1]
# 20
# nums[:]
# (10, 20, 30, 40)
# nums[1:]
# (20, 30, 40)
# 5 in nums
# False
# nums.index(30)
# 2
# some_list = [1, 1, 1]
# some_tuple = tuple(some_list)
# some_tuple
# (1, 1, 1)



#
# def get_user():
#     name = 'Bob'
#     surname ='Ivanov'
#     age = 20
#     return name, surname, age
# user = get_user()
# user
# ('Bob', 'Ivanov', 20)
#
#
#
# ('Vova', 'Petrov', 25)
# name, surname, age = user
# name
# 'Vova'
# surname
# 'Petrov'
# age
# 25