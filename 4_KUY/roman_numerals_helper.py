'''
https://www.codewars.com/kata/51b66044bce5799a7f000003
'''


class RomanNumerals:
    data1 = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50,
        'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    data2 = {'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}
    
    @staticmethod
    def to_roman(val: int) -> str:
        num, res, temp = 0, '', val
        while num != val:
            for i in RomanNumerals.data1:
                if RomanNumerals.data1[i] <= temp:
                    num += RomanNumerals.data1[i]
                    temp -= RomanNumerals.data1[i]
                    res += i
                    break
        return res

    @staticmethod
    def from_roman(roman_num: str) -> int:
        res = 0
        for i in roman_num:
            res += RomanNumerals.data1[i]
        for i in RomanNumerals.data2:
            if i in roman_num:
                res += RomanNumerals.data2[i]
        return res
