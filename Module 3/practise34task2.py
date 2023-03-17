first_class = []
second_class = []
result = []
for i_first in range(160,176,2):
    first_class.append(i_first)
print(first_class)
for i_second in range(162,180,3):
    second_class.append(i_second)
print(second_class)
result = first_class + second_class

result.sort()
print(result)

