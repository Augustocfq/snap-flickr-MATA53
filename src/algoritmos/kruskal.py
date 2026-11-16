def kruskal(n: int, edges: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    parent = list(range(n))
    rank = [0] * n

    def find(u: int) -> int:
        root = u
        while parent[root] != root:
            root = parent[root]
        while parent[u] != root:
            next_vertex = parent[u]
            parent[u] = root
            u = next_vertex
        return root

    tree = []
    for u, v, weight in sorted(edges, key=lambda edge: edge[2]):
        root_u, root_v = find(u), find(v)
        if root_u == root_v:
            continue
        if rank[root_u] < rank[root_v]:
            root_u, root_v = root_v, root_u
        parent[root_v] = root_u
        if rank[root_u] == rank[root_v]:
            rank[root_u] += 1
        tree.append((u, v, weight))
    return tree
