"""
https://www.codewars.com/kata/51c8e37cee245da6b40000bd
"""


def strip_comments(strng: str, markers):
    strng = strng.split('\n')
    answer = []
    for i in strng:
        line = ''
        for j in i:
            if j in markers:
                break
            else:
                line += j
        answer.append(line.rstrip())

    return '\n'.join(answer)


def main():
    print(strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))


if __name__ == '__main__':
    main()
