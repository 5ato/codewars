"""
https://www.codewars.com/kata/52742f58faf5485cae000b9a
"""


def to_other_time(seconds: int) -> tuple[int]:
    minute, seconds = divmod(seconds, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    return (year, day, hour, minute, seconds)


def format_duration(seconds: int) -> str:
    if seconds == 0: return 'now'
    words = ('year', 'day', 'hour', 'minute', 'second')
    time = to_other_time(seconds)
    result = [f'{t} {words[i]}s' if t > 1 else f'{t} {words[i]}' for i, t in enumerate(time) if t != 0]
    if len(result) == 1: return result[0]
    elif len(result) == 2: return f'{result[0]} and {result[1]}'
    else: return f'{", ".join(result[:-1])} and {result[-1]}'


if __name__ == '__main__':
    print(format_duration(3662))
