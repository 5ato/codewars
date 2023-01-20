"""
https://www.codewars.com/kata/52b7ed099cdc285c300001cd/
"""


def sum_of_intervals(intervals: list) -> int:
    intervals.sort()
    res = []
    start, end = intervals[0][0], intervals[0][1]

    for i in intervals[1::]:
        s, e = i[0], i[1]
        if s > end:
            res.append([start, end])
            start, end = s, e
        else:
            end = max(end, e)
    res.append([start, end])

    total = 0
    for i in res:
        total += (i[1] - i[0])
    return total


def main():
    pass


if __name__ == '__main__':
    main()
