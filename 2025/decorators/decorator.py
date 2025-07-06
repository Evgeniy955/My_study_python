import functools
from typing import Any


def deco_2(func):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("deco_2 before")
        result = func(*args, **kwargs)
        print("deca_2 after")
        return result

    return wrapper


def deco(func):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("deco before")
        result = func(*args, **kwargs)
        print("deco after")
        return result

    return wrapper

@deco
def my_function():
    return 1

@deco
def summator(a: int, b: int) -> int:
    return 1

@deco_2
@deco
def square(a: int) -> int:
    """
    Self multiple twice
    :param a: int
    :rerurn:
    """
    print('Function calling')
    return a * a

# print(square(1))
print(my_function())