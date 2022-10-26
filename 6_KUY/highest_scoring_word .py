"""
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
"""


def high(x: str) -> str:
    x = x.split()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index_alphabet = [i for i in range(1, 27)]
    hist = dict(zip(alphabet, index_alphabet))
    result = []
    for i in x:
        temp = 0
        for j in i:
            temp += hist[j]
        result.append((i, temp))
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return result[0][0]


def main():
    pass


if __name__ == '__main__':
    main()
