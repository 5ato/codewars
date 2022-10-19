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
    print(gcd(400, 320))


if __name__ == '__main__':
    main()
