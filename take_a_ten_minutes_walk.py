"""
https://www.codewars.com/kata/54da539698b8a2ad76000228
"""


def is_valid_walk(walk):
    if len(walk) == 10:
        cardinal_point = {'s': 1, 'n': -1, 'w': 2, 'e': -2}
        total = 0
        for i in walk:
            total = total + cardinal_point[i]
        if total == 0:
            return True
    return False


def main():
    print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))


if __name__ == '__main__':
    main()
