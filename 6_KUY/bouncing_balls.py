"""
https://www.codewars.com/kata/5544c7a5cb454edb3c000047
"""


def bouncing_balls(h: int, bounce: float, window: int or float) -> int:
    if (h > 0) and (0 < bounce < 1) and (window < h):
        count = 0
        while h > window:
            h = h * bounce
            count += 2
        return count - 1
    return -1


def main():
    print(bouncing_balls(30, 0.75, 1.5))


if __name__ == '__main__':
    main()
