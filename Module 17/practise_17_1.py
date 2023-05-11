from functools import reduce
from typing import List

float_list: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
str_list: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]


result = map(lambda num: round(num ** 3, 3), float_list)
print(list(result))

min_length = 5
filtered_list = list(filter(lambda word: len(word) >= min_length, str_list))
print(filtered_list)


def my_add(a: int, b: int) -> int:
    result = a + b

    print(f"{a} + {b} = {result}")

    return result

int_list: List[int] = [22, 33, 10, 6894, 11, 2, 1]

print(reduce(my_add, int_list))

