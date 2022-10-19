def lifo(string: str) -> bool:
    stack = []
    verify = True
    for i in string:
        if i in '({[':
            stack.append(i)
        elif i in ')]}':
            if len(stack) == 0:
                verify = False
                return verify
            br = stack.pop()
            if br == '(' and i == ')':
                continue
            if br == '[' and i == ']':
                continue
            if br == '{' and i == '}':
                continue
            verify = False
            return verify
    return verify


def main():
    print(lifo('((aboba) Любит [{(Abyrtish)}})'))


if __name__ == '__main__':
    main()
