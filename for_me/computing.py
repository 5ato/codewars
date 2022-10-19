def fibo(diapason: int) -> list:
    arr = []
    a, b = 0, 1
    for i in range(diapason):
        a, b = b, a+b
        arr.append(a)
    return arr


def memo_for_fibo(func):
    _cache = {}

    def wrapper(n):
        if n not in _cache:
            result = func(n)
            _cache[n] = result
            return result
        return _cache[n]
    return wrapper


# recursion
def fib_req(diapason: int) -> int:
    if diapason <= 1:
        return 1
    else:
        return fib_req(diapason-1) + fib_req(diapason-2)


# a % b
def mod(number1: int, number2: int) -> int:
    return number1 - (number1 // number2) * number2


# НОД(number1, number2)
def gcd(number1: int, number2: int) -> int:
    number1 = abs(number1)
    number2 = abs(number2)
    if number1 < number2:
        number1, number2 = number2, number1
    r = number1 % number2
    while r != 0:
        number1 = number2
        number2 = r
        r = number1 % number2
    return number2


def main():
    print(fib_req(13))


if __name__ == '__main__':
    main()
