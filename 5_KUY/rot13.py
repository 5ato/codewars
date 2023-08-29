alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet_lower.upper()


def rot13(message: str) -> str:
    result = ''
    for i in message:
        if i in alphabet_lower: result += alphabet_lower[(alphabet_lower.find(i) + 13) % 26]
        elif i in alphabet_upper: result += alphabet_upper[(alphabet_upper.find(i) + 13) % 26]
        else: result += i
    return result



if __name__ == '__main__':
    print(rot13('Test'))
