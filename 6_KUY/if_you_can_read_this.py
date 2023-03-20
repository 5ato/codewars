"""
https://www.codewars.com/kata/586538146b56991861000293
"""

NATO = {}


def to_nato(words: str) -> str:
    ' '.join(NATO.get(char, char) for char in words if char != ' ')


def main():
    to_nato('if you can read')


if __name__ == '__main__':
    main()
