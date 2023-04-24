go_to_coordinate = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
]


def in_map(x: int, y: int, length_map: list[list]) -> bool:
    return 0 <= x < length_map and 0 <= y < length_map


def snail(snail_map: list[list]) -> list:
    count_goto = 0
    x, y = 0 ,0
    result = [snail_map[y][x]]
    snail_map[y][x] = 0
    while True:
        tmp_x, tmp_y = go_to_coordinate[count_goto % 4](x, y)
        if (not in_map(tmp_x, tmp_y, len(snail_map))) or snail_map[tmp_y][tmp_x] == 0: 
            count_goto += 1
        else:
            x, y = tmp_x, tmp_y
            result.append(snail_map[y][x])
            snail_map[y][x] = 0
            if len(result) == len(snail_map) ** 2: return result
    

if __name__ == '__main__':
    print(snail([[1,2,3],
                 [4,5,6],
                 [7,8,9]]))
