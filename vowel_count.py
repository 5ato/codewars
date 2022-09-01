"""
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
"""


def get_count(sentence: str):
    count = 0
    for i in sentence:
        if i in 'aeiou':
            count += 1
    return count


def main():
    pass


if __name__ == '__main__':
    main()
