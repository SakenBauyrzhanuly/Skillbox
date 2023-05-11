from typing import List

my_nums: List[int] = [3, 1, 4, 1, 5, 9, 2, 6]
other_nums: List[int] = [2, 7, 1, 8, 2, 8, 1, 8]

result: List[int] = list(map(lambda x, y: x + y, my_nums, other_nums))

print(result)
# print(list(map(lambda x, y: 1, [1, 2], [2, 3, 4])))



result_even: List[int] = list(filter(lambda x: x % 2 == 0, result))
print(result_even)

result = map(lambda num: num * 3, filter(lambda num: num % 2, my_nums))

print(list(result))

result = sum(map(lambda num: num * 3, filter(lambda num: num % 2, my_nums)))
print(result)

# animals = ['cat', 'dog', 'cow']
# new_animals = list(map(lambda elem: elem.capitalize(), animals))
# print(new_animals)
#
# new_animals_list_comp = [elem.capitalize() for elem in animals]
# print(new_animals_list_comp)