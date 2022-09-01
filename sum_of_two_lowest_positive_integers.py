"""
https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
"""


def sum_two_smallest_numbers(numbers: list):
    return numbers.pop(numbers.index(min(numbers))) + min(numbers)


def find_small(numbers):
    small = numbers[0]
    small_index = 0
    for i in range(1, len(numbers)):
        if small > numbers[i]:
            small = numbers[i]
            small_index = i
    return small_index


def sum_two_smallest_numbers2(numbers):
    return numbers.pop(find_small(numbers)) + numbers.pop(find_small(numbers))


def main():
    pass


if __name__ == '__main__':
    main()
