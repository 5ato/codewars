class TArray:
    def __init__(self, count_elements: int, arr: list = []):
        self.count_elements: int = count_elements
        if self.clean_arr(count_elements, arr):
            self.arr: list = arr
        else:
            raise TypeError('Limit is exceeded')

    @classmethod
    def clean_arr(cls, count_elements, arr):
        if len(arr) > count_elements:
            return False
        return True

    def min_in_arr(self):
        min = self.arr[0]
        for item in self.arr:
            if min > item:
                min = item
        return min

    def max_in_arr(self):
        max = self.arr[0]
        for item in self.arr:
            if max > item:
                max = item
        return max

    def sort(self):
        swapped = False
        for i in range(self.count_elements-1):
            for j in range(0, self.count_elements-i-1):
                if self.arr[j] > self.arr[j+1]:
                    swapped = True
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
            if not swapped:
                return

    def __str__(self):
        return f'{self.arr}'

    def __add__(self, other):
        temp = self.arr.copy()
        temp = self.arr + [other]
        if self.clean_arr(self.count_elements, temp):
            self.arr = temp
            return TArray(self.count_elements, temp)
        else:
            raise TypeError('Limit is exceeded')

    def __mul__(self, other):
        temp = self.arr.copy()
        temp = temp * other
        if self.clean_arr(self.count_elements, temp):
            self.arr = temp
            return TArray(self.count_elements, temp)
        else:
            raise TypeError('Limit is exceeded')

def main():
    arr = TArray(12, [50, 120, 60, 74, 61, 97])


if __name__ == '__main__':
    main()
