class My_Fraction:
    def __init__(self, num: int, den: int):
        k = self.gcd(num, den)
        try:
            self.num: int = num // k
            self.den: int = den // k
        except ZeroDivisionError:
            print('Делить на 0 нельзя')

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __mul__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.num, self.den * other.den)
        if isinstance(other, int):
            return My_Fraction(self.num * other, self.den)
        return self

    def __truediv__(self, other):
        if isinstance(other, My_Fraction):
            return My_Fraction(self.num * other.den, self.den * other.den)
        if isinstance(other, int):
            return My_Fraction(self.num, self.den * other)


    @staticmethod
    def gcd(num: int, den: int) -> int:
        number1 = abs(num)
        number2 = abs(den)
        if number1 < number2:
            number1, number2 = number2, number1
        r = number1 % number2
        while r != 0:
            number1 = number2
            number2 = r
            r = number1 % number2
        return number2


def main():
    fract1 = My_Fraction(5, 10)
    fract2 = My_Fraction(2, 7)
    fract = fract1 * fract2
    print(fract)


if __name__ == '__main__':
    main()
