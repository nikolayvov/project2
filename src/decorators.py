from typing import Any, Callable, Optional


def write_log(message: str, filename: Optional[str] = None) -> None:
    """
                    Функция, которая определяет наличие лог-файла и запись в нем или
                    в консоли
                    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message)
    else:
        print(message)


def log(filename: Optional[str] = None) -> Callable:
    """
                Декоратор, который автоматически логирует начало и конец выполнения функции,
                 а также ее результаты или возникшие ошибки
                """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok {result}\n"
                write_log(message, filename)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e)}. args: {args}, kwargs: {kwargs}\n"
                write_log(message, filename)
                raise
        return wrapper
    return decorator


@log()
def my_function(x, y):
    return x + y


my_function(2, 3)
