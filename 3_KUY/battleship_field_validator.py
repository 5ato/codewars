def check_dots(*dots) -> bool:
    return all(0 <= i <= 9 for i in dots)


def radius_dot(x, y, field, k, d):
    count, dx, dy = 0, [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]
    for i in range(8):
        temp_y, temp_x = y + dy[i], x + dx[i]
        if check_dots(temp_x, temp_y):
            if field[temp_y][temp_x] == 1:
                count += 1
    if k == 0:
        if d == 1 and count >= 1: return False
        elif d >= 2 and count >= 2: return False
    elif k+1 == d:
        if count >= 1: return False
    elif k >= 1:
        if count > 2: return False
    return True


def validate_battlefield(field):
    ships = {4: 1, 3: 2, 2: 3, 1: 4}
    for d in sorted(ships.keys(), reverse=True):
        for i in range(10):
            for j in range(10-d+1):
                if all(field[i][j+x] for x in range(d)):
                    ships[d] -= 1
                    for x in range(d):
                        field[i][j + x] = 0
                        if not radius_dot(j+x, i, field, x, d): return False
        for i in range(10):
            for j in range(10-d+1):
                if all(field[j + x][i] == 1 for x in range(d)):
                    ships[d] -= 1
                    for x in range(d):
                        field[j + x][i] = 0
                        if not radius_dot(i, j+x, field, x, d): return False
    return all(ships[d] == 0 for d in ships)


if __name__ == '__main__':
    print(validate_battlefield([
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))
