from itertools import groupby

"""
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
"""


def group(args: list):
    for _, g in groupby(enumerate(args), key=lambda x: x[0]-x[-1]):
        r = [i for _, i in g]
        if len(r) > 2:
            yield f'{r[0]}-{r[-1]}'
        else:
            yield from map(str, r)


def solution(args: list) -> str:
    return ','.join(group(args))


def main():
    pass


if __name__ == '__main__':
    main()
