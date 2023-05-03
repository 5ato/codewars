from typing import Callable, Any


"""
https://www.codewars.com/kata/626a887e8a33feabd6ad8f25
"""


class predicate:
    def __init__(self, func: Callable):
        self.func: Callable = func
        
    def __call__(self, *args: Any, **kwargs: Any):
        return self.func(*args, **kwargs)
        
    def __and__(self, other: 'predicate'):
        def func(*args: Any, **kwargs: Any):
            return self.func(*args, **kwargs) and other.func(*args, **kwargs)
        return predicate(func)
    
    def __or__(self, other: 'predicate'):
        def func(*args: Any, **kwargs: Any):
            return self.func(*args, **kwargs) or other.func(*args, **kwargs)
        return predicate(func)
    
    def __invert__(self):
        def func(*args: Any, **kwargs: Any):
            return not self.func(*args, **kwargs)
        return predicate(func)


predicate = predicate


@predicate
def is_even(num):
    return num % 2 == 0

@predicate
def is_positive(num):
    return num > 0


if __name__ == '__main__':
    print((is_even & is_positive)(4))   # True
    print((is_even & is_positive)(3))   # False
    print((is_even | is_positive)(3) )  # True
    print((~is_even & is_positive)(3) ) # True
