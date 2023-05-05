from typing import Callable, Any
import time


# Реализация паттерна Decorator на основе класса первый вариант


class Decorator:
    def __init__(self, func: Callable):
        self.func: Callable = func

    def __call__(self, *args: Any, **kwargs: Any):
        start = time.perf_counter()
        result = self.func(*args, **kwargs)
        print(time.perf_counter() - start)
        return result


# Реализация паттерна Decorator с параметрами на основе класса второй вариант


class Decorator:
    def __init__(self, repeat: int = 1):
        self.repeat: int = repeat

    def __call__(self, func: Callable):
        start = time.perf_counter()
        def wrapper(*args: Any, **kwargs: Any):
            for _ in range(self.repeat):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                print(time.perf_counter() - start)
            return result
        print(time.perf_counter() - start)
        return wrapper
    
