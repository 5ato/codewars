"""
https://www.codewars.com/kata/55983863da40caa2c900004e
"""


def next_bigger(n: int) -> int:
    n = list(str(n))
    if len(n) == 1: return -1
    temp = list(i for i in range(1, len(n)) if n[i-1] < n[i])
    if not temp: return -1
    i = max(temp)
    j = max(j for j in range(i, len(n)) if n[i-1] < n[j])
    n[j], n[i-1] = n[i-1], n[j]
    n[i::] = reversed(n[i::])
    return int(''.join(n))


if __name__ == '__main__':
    print(next_bigger(21))
