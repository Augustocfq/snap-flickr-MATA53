import igraph as ig
import numpy as np


def compute_eccentricities_and_distance_sums(graph: ig.Graph) -> tuple[np.ndarray, np.ndarray]:
    n = graph.vcount()
    eccentricities = []
    distance_sums = []
    for start in range(0, n, 500):
        distances = np.array(graph.distances(source=range(start, min(start + 500, n))))
        eccentricities.append(distances.max(axis=1))
        distance_sums.append(distances.sum(axis=1))
    return np.concatenate(eccentricities), np.concatenate(distance_sums)
