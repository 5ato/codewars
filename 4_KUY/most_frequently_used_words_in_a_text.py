from string import ascii_letters


def next_and_previous(index: int, letter: str, word: str) -> bool:
    try: result = True if letter == "'" and ((word[index-1] in ascii_letters) or (word[index+1] in ascii_letters)) else False
    except: result = False
    return result


def top_3_words(text: str) -> list:
    my_text, result = '', {}
    for index, letter in enumerate(text):
        if letter in ascii_letters or next_and_previous(index, letter, text):
            my_text += letter.lower()
        else: my_text += ' '
    my_text = my_text.split()
    for word in my_text:
        if word not in result: result[word] = 1
        else: result[word] += 1
    return list(dict(sorted(result.items(), key=lambda x: x[1], reverse=True)).keys())[0:3]
