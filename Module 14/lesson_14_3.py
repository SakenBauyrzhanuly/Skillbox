import time
from typing import Callable, Any, List


def timer(func: Callable, list_of_some: List[int], *args, **kwargs) -> Callable:
    '''
    Декортаор. выводящий время, которое заняло выполнение декорируемой функции
    '''
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Функция работала {} секунды'.format(run_time))
        return result
    return wrapped_func




def time12r(sqwe: str, ad: int) -> HttpResponse:
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Функция работала {} секунды'.format(run_time))
        return result
    return fgtugtuygtuy

def time2r(ers, qwea, fsd) :
    '''
    Декортаор. выводящий время, которое заняло выполнение декорируемой функции
    '''
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print('Функция работала {} секунды'.format(run_time))
        return result
    return wrapped_func

@timer
def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**2 for i_num in range(10000)])

    return result

@timer
def cubes_sum(number: int) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num**3 for i_num in range(10000)])

    return result




my_sum = squares_sum()
print(my_sum)


my_cubes_sum = cubes_sum(200)
print(my_cubes_sum)