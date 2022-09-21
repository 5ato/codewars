def line_search(arr: list, element: int) -> int:
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1


def modification_line_search(arr: list, element: int) -> int:
    arr.append(element)
    i = 0
    while arr[i] != element:
        i += 1
    arr.pop()
    if len(arr) != i:
        return i
    return -1


def binary_search(arr: list, element: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        m = (left + right) // 2
        search_element = arr[m]
        if search_element > element:
            right = m - 1
        elif search_element < element:
            left = m + 1
        else:
            return m
    return -1


def exponential_search(arr: list, element: int) -> int:
    board = 1
    while board < len(arr) - 1 and arr[board] < element:
        board *= 2
    if board > len(arr) - 1:
        board = len(arr) - 1
    return binary_search(arr, element)


def ternary_search(arr: list, element: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        h = (right - left) // 3
        m1 = left + h
        m2 = right - h
        if arr[m1] == element:
            return m1
        if arr[m2] == element:
            return m2
        if arr[m1] < element < arr[m2]:
            left = m1 + 1
            right = m2 - 1
        elif element < arr[m1]:
            right = m1 - 1
        else:
            left = m2 + 1
    return -1


def interpolation_search(arr: list, element: int) -> int:
    left = 0
    right = len(arr) - 1
    while arr[left] < element < arr[right]:
        if arr[left] == arr[right]:
            break
        index = (element - arr[left]) * (left - right) // (arr[left] - arr[right]) + left
        if arr[index] > element:
            right = index - 1
        elif arr[index] < element:
            left = index + 1
        else:
            return index
    if arr[left] == element:
        return left
    if arr[right] == element:
        return right
    return -1


def main():
    pass


if __name__ == '__main__':
    main()
