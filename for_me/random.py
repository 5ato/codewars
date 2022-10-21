def find_matching_letters(s1: str, s2: str) -> str:
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = '1' if val1 > val2 else '2' if val2 > val1 else '='
            hist = -max(val1, val2), which + ':' + ch * max(val1, val2)
    return '/'.join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))


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
    pass


if __name__ == '__main__':
    main()
