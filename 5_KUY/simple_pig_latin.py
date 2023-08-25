from string import ascii_letters


def pig_it(text: str) -> str:
    return ' '.join(i[1::] + i[0] + 'ay' if len(i) > 1 else i + 'ay' if i in ascii_letters else i for i in text.split())


if __name__ == '__main__':
    print(pig_it('This is my string !'))
