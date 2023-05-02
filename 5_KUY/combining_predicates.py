from functools import update_wrapper


"""
https://www.codewars.com/kata/626a887e8a33feabd6ad8f25
"""


class P(object):
    def __init__(self, predicate):
        self.pred = predicate

    def __call__(self, *args, **kwargs):
        return self.pred(*args, **kwargs)

    def __and__(self, predicate):
        def func(*args, **kwargs):
            return self.pred(*args, **kwargs) and predicate(*args, **kwargs)
        return P(func)

    def __or__(self, predicate):
        def func(*args, **kwargs):
            return self.pred(*args, **kwargs) or predicate(*args, **kwargs)
        return P(func)

    def __invert__(self):
        def func(*args, **kwargs):
            return not self.pred(*args, **kwargs)
        return P(func)


def predicate(func):
    """Decorator that constructs a predicate (``P``) instance from
    the given function."""
    result = P(func)
    update_wrapper(result, func)
    return result


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
