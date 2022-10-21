class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet: str = alphabet
        self.key: str = key

    def key_len(self, text):
        result, i = '', 0
        while len(result) != len(text):
            result += self.key[i]
            if i == len(self.key)-1:
                i = 0
            else:
                i += 1
        return result

    def encode(self, text):
        key = self.key_len(text)
        result = []
        step = 0
        for i in text:
            if i in self.alphabet:
                result.append((self.alphabet.index(key[step]) + self.alphabet.index(i)) % len(self.alphabet))
                step += 1
        return ''.join([self.alphabet[i] for i in result])

    def decode(self, text):
        key = self.key
        result = []
        step = 0
        for i in text:
            if i in self.alphabet:
                decode = self.alphabet[self.alphabet.index(key[step]) - self.alphabet.index(i)]
                result.append(decode)
                step += 1
                key += decode
        return ''.join(result)


def main():
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)
    print(c.decode('rovwsoiv'))


if __name__ == '__main__':
    main()
