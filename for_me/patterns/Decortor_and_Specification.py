from typing import Any, Callable


class UnicDecorator:
    def __init__(self, func: Callable) -> None:
        self.func: Callable = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.func(*args, **kwargs)
    
    def __and__(self, other: 'UnicDecorator'):
        def func(*args, **kwargs) -> bool:
            return self.func(*args, **kwargs) and other.func(*args, **kwargs)
        return UnicDecorator(func)
    
    def __or__(self, other: 'UnicDecorator'):
        def func(*args, **kwargs) -> bool:
            return self.func(*args, **kwargs) or other.func(*args, **kwargs)
        return UnicDecorator(func)
    
    def __invert__(self):
        def func(*args, **kwargs) -> bool:
            return not self.func(*args, **kwargs)
        return func
    

@UnicDecorator
def is_even(num: int) -> bool:
    return (num % 2) == 0


@UnicDecorator
def is_positive(num: int) -> bool:
    return num > 0


@UnicDecorator
def is_equal(a: int, b: int) -> bool:
    return a == b


@UnicDecorator
def is_less_then(a: int, b: int) -> bool:
    return a < b


if __name__ == '__main__':
    print((is_even & is_positive)(50))
