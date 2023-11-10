import datetime
import typing
from functools import wraps


def log(*, filename: str = "") -> typing.Any:
    def wrapper(any_func: typing.Callable) -> typing.Callable:
        @wraps(any_func)
        def inner(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
            try:
                result = any_func(*args, **kwargs)
                if filename == "":
                    print(f"""{datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")} {any_func.__name__} ok""")
                    return result
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f'{datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")} {any_func.__name__} ok\n')
                    return result
            except Exception as error:
                print("Ошибка, см. лог файл")
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(
                        f'{datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")} {any_func.__name__} error: {error}. \
                         Inputs: {args}, {kwargs}\n'
                    )

        return inner

    return wrapper


@log(filename="../decorator_log.txt")
def my_function(x: typing.Any, y: typing.Any) -> typing.Any:
    """складывает два значения"""
    return x + y


print(my_function(None, None))
