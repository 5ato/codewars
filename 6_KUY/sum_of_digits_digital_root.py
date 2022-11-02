"""
https://www.codewars.com/kata/541c8630095125aba6000c00
"""


def digital_root(n: int) -> int:
    n = str(n)
    while len(n) != 1:
        temp = 0
        for i in n:
            temp += int(i)
        n = str(temp)
    return int(n)


def main():
    pass


if __name__ == '__main__':
    main()
