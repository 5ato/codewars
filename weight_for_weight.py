"""
https://www.codewars.com/kata/55c6126177c9441a570000cc
"""


def order_weight(strng: str) -> str:
    strng = sorted(strng.split())
    summing = []
    for i in strng:
        total = 0
        for j in i:
            total += int(j)
        summing.append(total)
    answer = sorted(zip(strng, summing), key=lambda x: x[1])
    return ' '.join([i[0] for i in answer])


def main():
    a = "2000 10003 1234000 44444444 9999 11 11 22 123"
    print(order_weight(a))


if __name__ == '__main__':
    main()
