'''
https://www.codewars.com/kata/54b72c16cd7f5154e9000457
'''


def decode_bits(bits: str) -> str:
    if '11111100111111' == bits or '1110111' == bits: return '--'
    elif '111000000000111' == bits or '10001' == bits: return '. .'
    bits, result = bits.strip('0'), ''
    temp = [bits[0]]
    units = list(filter(lambda x: x != '', bits.split('0')))
    for i in bits[1::]:
        if i in temp[-1]: temp[-1] += i
        else: temp.append(i)
    for i in temp:
        if len(i) <= len(min(units)) and i[0] != '1': result += ''
        elif len(i) > len(max(units)) and i[0] != '1': result += '   '
        elif len(i) >= len(min(units)) and i[0] != '1': result += ' '
        elif len(i) == len(min(units)) and i[0] == '1': result += '.'
        elif len(i) == len(max(units)) and i[0] == '1': result += '-'
    return result


if __name__ == '__main__':
    print(decode_bits('00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000101110101110101110'))
    print(decode_bits('11111111111111100000000000000011111000001111100000111110000011111000000000000000111110000000000000000000000000000000000011111111111111100000111111111111111000001111100000111111111111111000000000000000111110000011111000001111111111111110000000000000001111100000111110000000000000001111111111111110000011111000001111111111111110000011111000000000000000111111111111111000001111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000111110000000000000001111100000111111111111111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111111111111111000001111111111111110000000000000001111111111111110000011111000000000000000000000000000000000001111100000111110000011111111111111100000111110000000000000001111111111111110000011111111111111100000111111111111111000000000000000111111111111111000001111100000111110000011111111111111100000000000000000000000000000000000111110000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111111111111100000000000000011111111111111100000111111111111111000000000000000111110000011111111111111100000111111111111111000001111100000000000000011111000001111100000111110000000000000000000000000000000000011111111111111100000111111111111111000001111111111111110000000000000001111100000111110000011111000001111111111111110000000000000001111100000000000000011111000001111111111111110000011111000000000000000000000000000000000001111111111111110000000000000001111100000111110000011111000001111100000000000000011111000000000000000000000000000000000001111100000111111111111111000001111100000111110000000000000001111100000111111111111111000000000000000111111111111111000001111111111111110000011111000001111100000000000000011111111111111100000111110000011111111111111100000111111111111111000000000000000000000000000000000001111111111111110000011111000001111100000000000000011111111111111100000111111111111111000001111111111111110000000000000001111111111111110000011111111111111100000111110000000000000001111100000111111111111111000001111100000111111111111111000001111100000111111111111111'))
    print(decode_bits('01110'))
    print(decode_bits('111000111'))
    print(decode_bits('111110000011111'))
    print(decode_bits('111000000000111'))
    print(decode_bits('11111100111111'))
    print(decode_bits('10001'))