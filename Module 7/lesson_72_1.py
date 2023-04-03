import random
first_tuple = tuple(random.randint(0, 5) for i in range(10))

second_tuple = tuple(random.randint(-5, 0) for i in range(10))

third_tuple = first_tuple + second_tuple


print(first_tuple)
print(second_tuple)
print(third_tuple)
print(third_tuple.count(0))

