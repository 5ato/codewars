def max_sequence(arr: list[int]) -> int:
    max_sum, temp = 0, 0
    for i in arr:
        temp = temp + i
        temp = max(temp, 0)
        max_sum = max(temp, max_sum)
    return max_sum


if __name__ == '__main__':
    print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))
