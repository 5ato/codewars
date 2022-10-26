"""
https://www.codewars.com/kata/529adbf7533b761c560004e5
"""


def memo(func):
    _cache = {}

    def wrapper(n):
        if n not in _cache:
            result = func(n)
            _cache[n] = result
            return result
        return _cache[n]
    return wrapper


@memo
def fibonacci(n: int) -> int:
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    pass


if __name__ == '__main__':
    main()
