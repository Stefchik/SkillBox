from typing import Callable


def counter(func: Callable) -> Callable:
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f'{func.__name__} была вызвана: {wrapper.count} раз(а)')
        return res

    wrapper.count = 0
    return wrapper

@counter
def test_functions() -> None:
    print('Hello World!')

@counter
def test_functions2() -> None:
    print('I Am Groot')

test_functions()
test_functions2()
test_functions()
test_functions()
test_functions2()
test_functions()
