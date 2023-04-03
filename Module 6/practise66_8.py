def is_poly(string):
    char_dict = {}
    for i_sym in string:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1


    odd_count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1
    return  odd_count <= 1

my_string = input('Введите строку: ')
if is_poly(my_string):
    print('Можно сделать палиндром')
else:print('Нельзя')





def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
    return result

nums_n = [3, 3]
target = 6
twoSum(nums_n, target)
print(twoSum(nums_n, target))
