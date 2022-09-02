"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0
"""


def move_zeros1(lst):
    array_other_number = []
    array_zero_number = []
    for i in lst:
        if i == 0:
            array_zero_number.append(i)
        else:
            array_other_number.append(i)
    return array_other_number + array_zero_number


def move_zeros2(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]


def main():
    print(move_zeros1([1, 0, 1, 2, 0, 1, 3]))


if __name__ == '__main__':
    main()
