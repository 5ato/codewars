def select_sort(arr: list) -> list:
    new_list = []
    for _ in range(len(arr)):
        new_list.append(arr.pop(arr.index(min(arr))))
    return new_list


def insert_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else: break
    return arr


def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def main():
    print(insert_sort([5, 1, 8, 1, 3, 5, 1, 2, 3, 2, 4]))


if __name__ == '__main__':
    main()
