def select1_sort(arr: list) -> list:
    new_list = []
    for i in range(len(arr)):
        new_list.append(arr.pop(min(arr)))
    return new_list


def select2_sort(arr: list) -> list:
    for i in range(len(arr)-1):
        small = i
        for j in range(i+1, len(arr)):
            if small > j:
                small = j
        if small != i:
            temp = arr[i]
            arr[i] = arr[small]
            arr[small] = temp
    return arr


# class Cat:
#     def __init__(self, name: str, age: int) -> None:
#         self.name: str = name
#         self.age: int = age
#
#     def __str__(self):
#         return f'{self.name}: {self.age}'
#
#
# def substitution(element1: Cat, element2: Cat) -> int:
#     if element1 is not None and element2 is None:
#         return 1
#     if element1 is None and element2 is not None:
#         return -1
#     if element1 is None and element2 is None:
#         return 0
#     if element1.age > element2.age:
#         return 1
#     if element1.age < element2.age:
#         return -1
#     return 0
#
#
# def cat_select_sort(arr: list) -> list:
#     for i in range(len(arr)-1):
#         small = i
#         for j in range(i+1, len(arr)):
#             if substitution(arr[small], arr[j]) > 0:
#                 small = j
#         if small != i:
#             temp = arr[i]
#             arr[i] = arr[small]
#             arr[small] = temp
#     return arr


def my_bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    swapping = True
    consolidation = -1
    while swapping:
        swapping = False
        consolidation += 1
        for i in range(1, len(arr)-consolidation):
            if arr[i-1] > arr[i]:
                swap(i-1, i)
                swapping = True
    return arr


def main():
    pass


if __name__ == '__main__':
    main()
