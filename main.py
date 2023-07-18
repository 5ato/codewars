from string import ascii_letters


# index_end, symbol, swapped = -1, '', True
# if word[-1] not in ascii_letters: index_end, symbol = -2, word[-1]
        # while swapped:
        #     swapped = False
        #     for i in range(len(temp)-1):
        #         if (temp[i] not in ascii_letters) or (temp[i+1] not in ascii_letters): continue
        #         if temp[i] > temp[i+1]: 
        #             temp[i], temp[i+1], swapped = temp[i+1], temp[i], True


def scramble_words(words: str) -> str:
    words, result = words.split(), []
    for word in words:
        temp, symbols = '', []
        for letter in word:
            if letter not in ascii_letters: 
                symbols.append([letter, word.index(letter)])
                continue
            temp += letter
        start, end = temp[0], temp[-1]
        temp = sorted(list(temp[1:-1]))
        temp.insert(0, start)
        temp.append(end)
        for j in symbols:
            temp.insert(j[1], j[0])
        result.append(''.join(temp))
    return ' '.join(result)


if __name__ == '__main__':
    print(scramble_words(
        "watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.")
         == "wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth."
        )
