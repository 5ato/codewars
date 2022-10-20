"""
https://www.codewars.com/kata/54e6533c92449cc251001667
"""

from itertools import groupby


def order1(iterable):
    iterable += 'a'
    return [iterable[i] for i in range(len(iterable)-1) if iterable[i] != iterable[i+1]]


def order2(iterable):
    return [_ for _, g in groupby(iterable)]


def main():
    pass


if __name__ == '__main__':
    main()