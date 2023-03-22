"""
https://www.codewars.com/kata/5839c48f0cf94640a20001d3
"""


def land_perimeter(arr: list[str]) -> int:    
    total = 0
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 'X':
                total += 4
                if (y != len(arr)-1) and (arr[y+1][x] == 'X'): total -= 1
                if (y != 0) and (arr[y-1][x] == 'X'): total -= 1
                if (x != len(arr[y])-1) and (arr[y][x+1] == 'X'): total -= 1
                if (x != 0) and (arr[y][x-1] == 'X'): total -= 1
    return total


if __name__ == '__main__':
    print(land_perimeter(['XOOXO',
                          'XOOXO',
                          'OOOXO',
                          'XXOXO',
                          'OXOOO']))
