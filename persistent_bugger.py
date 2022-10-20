"""
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
"""


def persistence(n):
    n = str(n)
    count = 0
    while len(n) != 1:
        temp = 1
        for i in n:
            temp *= int(i)
        n = str(temp)
        count += 1
    return count


def main():
    pass


if __name__ == '__main__':
    main()
