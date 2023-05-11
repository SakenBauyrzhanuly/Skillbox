import random

nums = [random.randint(0, 10) for _ in range(10)]
pairs = [(nums[i], nums[i + 1]) for i in range(0, len(nums)-1, 2)]

# res = []
# for i in range(len(nums)):
#     if i % 2 == 0:
#         res.append((nums[i], nums[i + 1]))

# length = len(nums) // 2
# res = []
# a = 0
# b = 1
# for _ in range(length):
#     res.append((nums[a], nums[b]))
#     a += 2
#     b += 2
#
#
print(nums)
print(pairs)
