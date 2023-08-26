def make_readable(seconds: int) -> str:
    hour, minut, second = str((seconds // 60) // 60), str((seconds // 60) % 60), str(seconds % 60)
    return ':'.join(i if len(i) == 2 else '0' + i for i in (hour, minut, second))


if __name__ == '__main__':
    print(make_readable(238141))
