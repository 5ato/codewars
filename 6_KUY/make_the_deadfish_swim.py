"""
https://www.codewars.com/kata/51e0007c1f9378fa810002a9
"""


def parse(data: str) -> list:
    result = []
    ops = {
        'i': lambda x: x + 1,
        'd': lambda x: x - 1,
        's': lambda x: x ** 2,
        'o': None
    }
    temp = 0
    for i in data:
        if i in ops:
            if i != 'o':
                temp = ops[i](temp)
            else:
                result.append(temp)
    return result


def main():
    print(parse('ioioio'))


if __name__ == '__main__':
    main()
