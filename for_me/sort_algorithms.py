def select_sort(arr: list) -> list:
    new_list = []
    for _ in range(len(arr)):
        new_list.append(arr.pop(arr.index(min(arr))))
    return new_list


def bubble_sort(arr):
    swapping = True
    consolidation = -1
    while swapping:
        swapping = False
        consolidation += 1
        for i in range(1, len(arr)-consolidation):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapping = True
    return arr


def main():
    print(bubble_sort([5, 1, 8, 1, 3, 5, 1, 2, 3, 2, 4]))


if __name__ == '__main__':
    main()
