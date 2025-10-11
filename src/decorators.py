import time
from functools import wraps
from typing import Any, Callable


def log(filename: None = None) -> Callable:
    """Декоратор, который автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def wrapper(func: Callable) -> Any:
        @wraps(func)
        def inner(*args: tuple[Any], **kwargs: dict[str, Any]) -> Any:
            try:
                time_1 = time.perf_counter()
                result = func(*args, **kwargs)
                time_2 = time.perf_counter()
                if filename:
                    with open("mylog.txt", "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open("mylog.txt", "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
        return inner

    return wrapper

@log()
def my_function(x, y):
    return x + y

my_function(5, 2)