from typing import Iterable


def get_link(current: int, graph: Iterable[Iterable[int]]) -> int:
    for j, weight in enumerate(graph[current]):
        if weight > 0:
            yield j


def arg_min(result: list[int], story: set[int]) -> int:
    amin, m = -1, max(result)
    for j, w in enumerate(result):
        if w < m and j not in story:
            m, amin = w, j
    return amin


def dijkstra(graph: Iterable[Iterable[int]]) -> list[int]:
    n = len(graph)
    result = [100000] * n
    current = 0
    story = {current}
    result[current] = 0

    while current != -1:
        for i in get_link(current, graph):
            if i not in story:
                weight = result[current] + graph[current][i]
                if weight < result[i]:
                    result[i] = weight
        
        current = arg_min(result, story)
        if current > 0:
            story.add(current)
    return result


if __name__ == '__main__':
    print(dijkstra(
            (
                (0, 7, 7, 0, 0, 0),
                (0, 0, 0, 4, 3, 0),
                (0, 5, 0, 0, 10, 0),
                (0, 0, 0, 0, 0, 8),
                (0, 0, 0, 11, 0, 4),
                (0, 0, 0, 0, 0, 0)
            )
        )
    )
