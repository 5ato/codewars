def dfs(graph: dict, start: str, visited: list = []):
    if start not in visited:
        visited.append(start)
        for neighbour in graph[start]:
            dfs(graph, neighbour, visited)


def bfs(graph: dict, start: str) -> list[str]:
    queue = [start]
    visited = [start]

    while queue:
        s = queue.pop(0)

        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

    return visited


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}


if __name__ == '__main__':
    print(bfs(graph, 'A'))
