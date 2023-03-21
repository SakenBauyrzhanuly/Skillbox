import random

N = [random.randint(0, 10) for i in range(10)]

res = [1 if j % 2 != 0 else N[j] % 5 for j in range(len(N))]

print(res)