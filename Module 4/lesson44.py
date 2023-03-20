# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] = 0
#
# for i_elem in range(2, 8):
#     print(nums[i_elem], end = ' ')
#
# print()
#
# for i_elem in range(2, 8):
#     print(new_nums[i_elem], end = ' ')



print('-------------')
# nums = [x for x in range(1, 101) if x % 10 == 0]
# new_nums = nums[:]
# new_nums[3] = 0
#
# print(new_nums[2:8])


print('-------------')

def is_palindrome(num_list):
    reverse_list = num_list[::-1]
    if num_list == reverse_list:
        return  True
    else:
        return False


nums = [1, 2, 1, 2, 2]
answer = []
for i_nums in range(0,len(nums)):
    if is_palindrome(nums[i_nums:len(nums)]):
        answer = nums[:i_nums]
        answer.reverse()
        break

print('Исходный список: ',nums)
print('Нужный чисел для палиндрома: ',len(answer))
print('Список этих чисел:',answer)