import numpy as np


def floyd_warshall(n: int, edges: list[tuple[int, int, int]]) -> np.ndarray:
    distances = np.full((n, n), np.inf)
    np.fill_diagonal(distances, 0)
    for u, v, weight in edges:
        distances[u, v] = weight
        distances[v, u] = weight
    for k in range(n):
        np.minimum(distances, distances[:, [k]] + distances[[k], :], out=distances)
    return distances
