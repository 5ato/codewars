"""
https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3
"""


class VigenereCipher:
    def __init__(self, key: str, alphabet: str) -> None:
        self.key: str = key
        self.alphabet: str = alphabet

    def key_len(self, text: str) -> str:
        result = ''
        i = 0
        while len(result) != len(text):
            result += self.key[i]
            if i < len(self.key)-1:
                i += 1
            else:
                i = 0
        return result

    def encode(self, text: str) -> str:
        result = []
        key = self.key_len(text)
        index = 0
        for i in text:
            if i in self.alphabet:
                text_alphabet = self.alphabet.index(i)
                key_alphabet = self.alphabet.index(key[index])
                result.append(self.alphabet[(text_alphabet + key_alphabet) % len(self.alphabet)])
                index += 1
            else:
                index += 1
                result.append(i)
        return ''.join(result)

    def decode(self, text: str) -> str:
        result = []
        key = self.key_len(text)
        index = 0
        for i in text:
            if i in self.alphabet:
                text_alphabet = self.alphabet.index(i)
                key_alphabet = self.alphabet.index(key[index])
                decoded = self.alphabet[(text_alphabet - key_alphabet) % len(self.alphabet)]
                result.append(decoded)
                index += 1
            else:
                index += 1
                result.append(i)
        return ''.join(result)


def main():
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)
    print(c.encode('codewars'))


if __name__ == '__main__':
    main()
