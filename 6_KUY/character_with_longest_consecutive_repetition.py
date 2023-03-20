"""
https://www.codewars.com/kata/586d6cefbcc21eed7a001155
"""


def longest_repetition(chars: str) -> tuple[str, int]:
    result = ('', 0)
    current = ['', 0]
    for char in chars:
        if current[0] == char: current[1] += 1
        else: current = [char, 1]

        if current[1] > result[1]: result = (char, current[1])
    
    return result


def main():
    print(longest_repetition('aaaaabbbba'))


if __name__ == '__main__':
    main()
