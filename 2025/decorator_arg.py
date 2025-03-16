import functools
import time
from typing import Any



def logger(name: str):
    def inner(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            print(f'{name}: {time.perf_counter() - start_time}')
            return result
        return wrapper

    return inner



@logger('square')
def square(a: int) -> int:
    """
    Self multiple twice
    :param a: int
    :rerurn:
    """
    print('Function calling')
    return a * a

square(1)