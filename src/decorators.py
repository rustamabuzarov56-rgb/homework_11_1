from functools import wraps
import time


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                time_1 = time.perf_counter()
                result = func(*args, **kwargs)
                time_2 = time.perf_counter()
                print(f"Time execution: {time_2 - time_1}")
                if filename:
                    with open("mylog.txt", "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
        return inner
    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

my_function(4, 2)