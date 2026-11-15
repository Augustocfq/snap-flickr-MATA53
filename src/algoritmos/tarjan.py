def find_articulation_points_and_bridges(
    adjacency: list[list[int]],
) -> tuple[set[int], set[tuple[int, int]]]:
    n = len(adjacency)
    discovery = [-1] * n
    low = [0] * n
    articulation_points = set()
    bridges = set()
    next_discovery = 0
    for root in range(n):
        if discovery[root] != -1:
            continue
        discovery[root] = low[root] = next_discovery
        next_discovery += 1
        root_children = 0
        stack = [(root, -1, iter(adjacency[root]))]
        while stack:
            u, parent, neighbors = stack[-1]
            for v in neighbors:
                if discovery[v] == -1:
                    discovery[v] = low[v] = next_discovery
                    next_discovery += 1
                    stack.append((v, u, iter(adjacency[v])))
                    break
                if v != parent:
                    low[u] = min(low[u], discovery[v])
            else:
                stack.pop()
                if parent == -1:
                    continue
                low[parent] = min(low[parent], low[u])
                if low[u] > discovery[parent]:
                    bridges.add((min(parent, u), max(parent, u)))
                if parent == root:
                    root_children += 1
                elif low[u] >= discovery[parent]:
                    articulation_points.add(parent)
        if root_children >= 2:
            articulation_points.add(root)
    return articulation_points, bridges
