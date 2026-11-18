import numpy as np

from src.algoritmos.buscas import breadth_first_search


def average_clustering(adjacency: list[list[int]]) -> float:
    neighbor_sets = [set(neighbors) for neighbors in adjacency]
    twice_triangles = [0] * len(adjacency)
    for u, neighbors in enumerate(adjacency):
        for v in neighbors:
            if u < v:
                common_neighbors = len(neighbor_sets[u] & neighbor_sets[v])
                twice_triangles[u] += common_neighbors
                twice_triangles[v] += common_neighbors
    clustering_sum = 0.0
    for u, neighbors in enumerate(adjacency):
        k = len(neighbors)
        if k >= 2:
            clustering_sum += twice_triangles[u] / (k * (k - 1))
    return clustering_sum / len(adjacency)


def average_distances_from_sources(adjacency: list[list[int]], sources: list[int]) -> np.ndarray:
    n = len(adjacency)
    return np.array([sum(breadth_first_search(adjacency, source)) / (n - 1) for source in sources])
