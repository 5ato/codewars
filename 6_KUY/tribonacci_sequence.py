"""
https://www.codewars.com/kata/556deca17c58da83c00002db
"""


def tribonacci_my(signature: list[int], n: int):
    count = 0
    for _ in signature:
        if count+3 < n:
            signature.append(sum(signature[count:len(signature)]))
            count += 1
            continue
        break
    if n == 0:
        signature = []
    elif n == 1:
        signature = [signature[0]]
    elif n == 2:
        signature = signature[0:-1]
    return signature


def tribonacci_normal(signature: list[int], n: int) -> list[int]:
    res = signature[:n]
    for _ in range(n-3):
        res.append(sum(res[-3:]))
    return res


if __name__ == '__main__':
    print(tribonacci_normal([300, 200, 100], 0))
            