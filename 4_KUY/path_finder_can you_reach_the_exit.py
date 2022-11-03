"""
https://www.codewars.com/kata/5765870e190b1472ec0022a2
"""


def path_finder(maze: str) -> bool:
    maze = maze.split('\n')
    m = len(maze)
    n = len(maze[-1])
    point = [0, 0]
    finish = [n-1, m-1]
    used = [[False] * n for _ in range(m)]
    used[0][0] = True
    queue = [point]
    delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < m) and not used[ny][nx] and maze[ny][nx] != 'W':
                if [nx, ny] == finish:
                    return True
                else:
                    used[ny][nx] = True
                    queue.append([nx, ny])
    return False


def main():
    a = "\n".join([
        ".W...",
        ".W...",
        ".W.W.",
        "...W.",
        "...W."])
    print(path_finder(a))


if __name__ == '__main__':
    main()
