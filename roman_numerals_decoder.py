def solution(roman):
    roman1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman2 = {'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}
    answer = 0
    for i in roman:
        answer += roman1[i]
    for i in roman2:
        if i in roman:
            answer += roman2[i]
    return answer


def main():
    pass


if __name__ == '__main__':
    main()
