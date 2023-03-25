"""
https://www.codewars.com/kata/61fef3a2d8fa98021d38c4e5
"""


def card_game(n: int) -> list[int, bool]:
    t, s = 0, n + 2
    while s > 3:
        s, t = s // 2, t+1+s % 2
    return [n-t, t][n % 2]


def main():
    print(card_game(100_000_000_000))


if __name__ == '__main__':
    main()
