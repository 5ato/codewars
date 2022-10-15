"""
https://www.codewars.com/kata/545cedaa9943f7fe7b000048
"""


def is_pangram(s: str) -> bool:
    result = []
    for i in s:
        if i.lower() not in result and i.isalpha():
            result.append(i.lower())
    result = ''.join(sorted(result))
    return True if result == 'abcdefghijklmnopqrstuvwxyz' else False


def main():
    pass


if __name__ == '__main__':
    main()
