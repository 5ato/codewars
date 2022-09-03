"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362
"""


def likes1(names: list) -> str:
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'


def likes2(names):
    length = len(names)
    answer_dict = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }
    return answer_dict[min(4, length)].format(*names[:3], others=length-2)


def main():
    print(likes2(["Max", "John", "Mark"]))


if __name__ == '__main__':
    main()
