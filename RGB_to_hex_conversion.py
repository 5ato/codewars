"""
https://www.codewars.com/kata/513e08acc600c94f01000001
"""


def rgb1(r, g, b):
    convert = [i if i > 0 else 0 for i in (r, g, b)]
    convert = ['%X' % i if i < 255 else 'FF' for i in convert]
    convert = [i if len(i) == 2 else '0' + i for i in convert]
    return ''.join(convert)


def rgb2(r, g, b):
    check = lambda x: min(255, max(x, 0))
    return '%02X%02X%02X' % (check(r), check(g), check(b))


def main():
    print(rgb2(-1, 55, 267))


if __name__ == '__main__':
    main()
