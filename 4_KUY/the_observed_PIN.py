"""
https://www.codewars.com/kata/5263c6999e0f40dee200059d
"""
import itertools


def get_pins(observed: str) -> list:
    path = {'1': '124', '2': '2153', '3': '326',
            '4': '4157', '5': '52486', '6': '6359',
            '7': '748', '8': '85709', '9': '968', '0': '08'}
    data = []
    for i in observed:
        temp = path[i]
        result_temp_list = []
        for j in temp:
            result_temp_list.append(j)
        data.append(result_temp_list)

    result = []
    for i in itertools.product(*data):
        result.append(''.join(i))

    return result


def main():
    print(get_pins('369'))


if __name__ == '__main__':
    main()
