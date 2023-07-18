from string import ascii_letters


def scramble_words(words: str) -> str:
    words, result = words.split(), []
    for word in words:
        temp, symbols = '', []
        for letter in word:
            if letter not in ascii_letters: 
                symbols.append([letter, word.index(letter)])
                continue
            temp += letter
        if len(temp) == 1:
            result.append(temp)
            continue
        start, end = temp[0], temp[-1]
        temp = sorted(list(temp[1:-1]))
        temp.insert(0, start)
        temp.append(end)
        for j in symbols:
            temp.insert(j[1], j[0])
        result.append(''.join(temp))
    return ' '.join(result)
