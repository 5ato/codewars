"""
https://www.codewars.com/kata/581bc0629ad9ff9873000316
"""


def token(string: str) -> list or str:
    result = []
    curr = ''
    for i in string:
        if i.isdigit() or i == '.':
            curr += i
        elif i in '$*-+':
            result.extend([float(curr), i])
            curr = ''
        else:
            raise ValueError('404: Bad request')
    if curr:
        result.append(float(curr))
    return result


def calculator(string: str) -> list or str:
    ops = {
        '$': lambda x, y: x / y,
        '*': lambda x, y: x * y,
        '-': lambda x, y: x - y,
        '+': lambda x, y: x + y,
    }

    try:
        tokenize = token(string)
        print(tokenize)
    except ValueError:
        return '404: Bad request'

    for op in '$*-+':
        while op in tokenize:
            i = tokenize.index(op)
            tokenize = tokenize[:i-1] + [ops[op](tokenize[i-1], tokenize[i+1])] + tokenize[i+2:]

    return tokenize[0]


def main():
    print(calculator('50$2+40*5-100000$40'))


if __name__ == '__main__':
    main()
