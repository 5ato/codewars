"""
https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
"""

import re


def to_camel_case(text: str) -> str:
    return text[0] + ''.join(item.title() for item in re.split('[-|_]', text)[1::])


def main():
    print(to_camel_case("the_stealth-warrior"))


if __name__ == '__main__':
    main()
