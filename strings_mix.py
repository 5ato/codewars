"""
https://www.codewars.com/kata/5629db57620258aa9d000014
"""


def mix(s1: str, s2: str):
    array = []
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if s1.count(i) >= 2 and s1.count(i) > s2.count(i):
            array.append(f'1:{i * s1.count(i)}')
        if s1.count(i) == s2.count(i) and (s1.count(i) >= 2 and s2.count(i) >= 2):
            array.append(f'=:{i * s1.count(i)}')
            array.sort()
        if s2.count(i) >= 2 and s2.count(i) > s1.count(i):
            array.append(f'2:{i * s2.count(i)}')
            array.sort()

    return '/'.join(sorted(array, key=len, reverse=True))


def main():
    s1 = "my&friend&Paul has heavy hats! &"
    s2 = "my friend John has many many friends &"
    print(mix(s1, s2))


if __name__ == '__main__':
    main()
