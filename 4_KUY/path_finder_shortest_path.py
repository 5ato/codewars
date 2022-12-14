"""
https://www.codewars.com/kata/57658bfa28ed87ecfa00058a
"""


def path_finder(maze: str) -> bool or int:
    maze = maze.split('\n')
    if len(maze) == 1 and maze[0][0] == '.':
        return 0
    m = len(maze)
    n = len(maze[0])
    used = [[False for i in range(n)] for j in range(m)]
    used[0][0] = True
    max_number = 10 ** 9
    count_path = [[max_number] * n for _ in range(m)]
    queue = [[0, 0]]
    finish = [n-1, m-1]
    count_path[0][0] = 0
    delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not used[ny][nx] and maze[ny][nx] != 'W':
                if [nx, ny] == finish:
                    count_path[ny][nx] = count_path[y][x] + 1
                    return count_path[finish[0]][finish[1]]
                else:
                    count_path[ny][nx] = count_path[y][x] + 1
                    used[ny][nx] = True
                    queue.append([nx, ny])

    return False


def main():
    a = "\n".join([
        ".W.",
        ".W.",
        "..."
    ])
    print(path_finder(a))


if __name__ == '__main__':
    main()
