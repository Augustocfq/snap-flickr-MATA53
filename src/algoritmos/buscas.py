from collections import deque


def build_adjacency(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    return adjacency


def breadth_first_search(adjacency: list[list[int]], source: int) -> list[int]:
    distances = [-1] * len(adjacency)
    distances[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                queue.append(v)
    return distances


def depth_first_search(adjacency: list[list[int]], source: int) -> list[int]:
    was_visited = [False] * len(adjacency)
    visit_order = []
    stack = [source]
    while stack:
        u = stack.pop()
        if was_visited[u]:
            continue
        was_visited[u] = True
        visit_order.append(u)
        stack.extend(v for v in adjacency[u] if not was_visited[v])
    return visit_order
