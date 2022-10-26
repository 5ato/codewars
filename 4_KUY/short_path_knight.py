"""
https://www.codewars.com/kata/549ee8b47111a81214000941
"""


x_chess = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8
}
y_chess = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8
}


def is_inside(x: int, y: int) -> bool:
    if (1 <= x <= 8) and (1 <= y <= 8):
        return True
    return False


class Coordinate:
    def __init__(self, x: str or int, y: str or int, dist: int = 0) -> None:
        self.x: int = x_chess[x]
        self.y: int = y_chess[y]
        self.dist: int = dist


def knight(p1: str, p2: str) -> int:
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    visited = set()
    p1 = Coordinate(p1[0], p1[1], 0)
    p2 = Coordinate(p2[0], p2[1], 0)

    queue = [p1]

    while len(queue) > 0:
        temp = queue.pop()
        x = temp.x
        y = temp.y
        dist = temp.dist

        if x == p2.x and y == p2.y:
            return dist

        if temp not in visited:
            visited.add(temp)
            for i in range(8):
                x1 = x + dx[i]
                y1 = y + dy[i]

                if is_inside(x1, y1):
                    queue.append(Coordinate(x1, y1, dist + 1))


def main():
    print(knight('a1', 'c1'))


if __name__ == '__main__':
    main()
