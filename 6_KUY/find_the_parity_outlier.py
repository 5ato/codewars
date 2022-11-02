"""
https://www.codewars.com/kata/5526fc09a1bbd946250002dc
"""


def find_outlier(integers: list[int]) -> int:
    even = [i for i in integers if i % 2 == 0]
    odd = [i for i in integers if i % 2 != 0]
    return even[0] if len(even) == 1 else odd[0]


def main():
    pass


if __name__ == '__main__':
    main()
