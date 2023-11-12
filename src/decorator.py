import datetime
import typing
from functools import wraps


def log(*, filename: str = "") -> typing.Any:
    def wrapper(any_func: typing.Callable) -> typing.Callable:
        @wraps(any_func)
        def inner(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
            date_now = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
            try:
                result = any_func(*args, **kwargs)
                log_message = f"""{date_now} {any_func.__name__} ok"""
            except Exception as error:
                log_message = f"""{date_now} {any_func.__name__} error: <{error}>. Inputs: {args}, {kwargs}"""
                result = None
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return inner

    return wrapper


@log(filename="../decorator_log.txt")
def my_function(x: typing.Any, y: typing.Any) -> typing.Any:
    """складывает два значения"""
    return x + y


print(my_function("1", 1))
