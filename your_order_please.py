"""
https://www.codewars.com/kata/55c45be3b2079eccff00010f
"""


def order(string: str) -> str:
    if len(string) == 0:
        return ''
    hist = {}
    string = string.split()
    for i in string:
        for j in i:
            if j.isdigit():
                hist[int(j)] = string[string.index(i)]
    hist = sorted(hist.items(), key=lambda x: x[0])
    return ' '.join(dict(hist).values())


def main():
    print(order("is2 Thi1s T4est 3a"))


if __name__ == '__main__':
    main()
