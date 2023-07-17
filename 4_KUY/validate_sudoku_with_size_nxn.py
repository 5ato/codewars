"""
https://www.codewars.com/kata/540afbe2dc9f615d5e000425
"""


class Sudoku:
    def __init__(self, data: list[list[int]]) -> None:
        self.data: list[list[int]] = data
        self.row: int = len(data[0])
        self.column: int = len(data)

    def valid_size(self) -> bool:
        if self.column == 1: return False
        if self.data[0][0] == 1: return True
        validate_item = self.data[0]
        for i in self.data:
            if len(i) != len(validate_item): return False
        return True

    def is_valid(self) -> bool:
        if not self.valid_size(): return False
        for row1 in self.data:
            index_row1 = self.data.index(row1)
            for item in row1:
                index_item = row1.index(item)
                if index_item == 0:
                    if item in row1[index_item+1::]: return False
                elif index_item == len(row1)-1:
                    if item in row1[0:index_item]: return False
                elif 0 < index_item < len(row1)-1:
                    if (item in row1[0:index_item]) and (item in row1[index_item+1::]): return False
                for row2 in self.data:
                    index_row2 = self.data.index(row2)
                    if index_row2 == index_row1: continue
                    if row2[index_item] == item: return False
        return True


if __name__ == '__main__':
    good_s1 = Sudoku([
    [7,8,4,  1,5,9,  3,2,6],
    [5,3,9,  6,7,2,  8,4,1],
    [6,1,2,  4,3,8,  7,5,9],
    
    [9,2,8,  7,1,5,  4,6,3],
    [3,5,7,  8,4,6,  1,9,2],
    [4,6,1,  9,2,3,  5,8,7],
    
    [8,7,6,  3,9,4,  2,1,5],
    [2,4,3,  5,6,1,  9,7,8],
    [1,9,5,  2,8,7,  6,3,4],
])

    good_s2 = Sudoku([
    [1,4, 2,3],
    [3,2, 4,1],
    
    [4,1, 3,2],
    [2,3, 1,4],
])
    
    good_s3 = Sudoku([[1]])

    bad_s1 = Sudoku([
    [0,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
    [1,2,3, 4,5,6, 7,8,9],
])

    bad_s2 = Sudoku([
    [1,2,3,4,5],
    [1,2,3,4],
    [1,2,3,4],
    [1]
])
    
    print(good_s2.is_valid())
    print(bad_s1.is_valid())
    print(good_s3.is_valid())


[[1, 2, 3, 4, 5, 6, 7, 8, 9],
[2, 3, 1, 5, 6, 4, 8, 9, 7],
[3, 1, 2, 6, 4, 5, 9, 7, 8],
[4, 5, 6, 7, 8, 9, 1, 2, 3],
[5, 6, 4, 8, 9, 7, 2, 3, 1],
[6, 4, 5, 9, 7, 8, 3, 1, 2],
[7, 8, 9, 1, 2, 3, 4, 5, 6],
[8, 9, 7, 2, 3, 1, 5, 6, 4],
[9, 7, 8, 3, 1, 2, 6, 4, 5]],
