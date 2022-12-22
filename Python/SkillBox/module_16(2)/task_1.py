from functools import wraps
from typing import Callable

def check_permission(user_name: str) -> Callable:
    """
    Декоратор для проверки прав пользователя.
    Возвращает ошибку или право доступа к функции
    """
    ADMINS_LIST = ['admin']

    def check_permission_2(func: Callable) -> Callable:
        @wraps(func)
        def wrapped(*args, **kwargs) -> Callable:
            try:
                if user_name in ADMINS_LIST:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print('PermissionError: У пользователя недостаточно прав,'
                      f' чтобы выполнить функцию {func.__name__}')

        return wrapped

    return check_permission_2

@check_permission('admin')
def delete_site() -> None:
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')

delete_site()
add_comment()
