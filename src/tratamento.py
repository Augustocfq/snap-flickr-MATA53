import numpy as np
from scipy.sparse import coo_array
from scipy.sparse.csgraph import connected_components


def remove_self_loops(edges: np.ndarray) -> np.ndarray:
    return edges[edges[:, 0] != edges[:, 1]]


def remove_duplicate_edges(edges: np.ndarray) -> np.ndarray:
    return np.unique(np.sort(edges, axis=1), axis=0)


def reindex_vertices(edges: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    original_ids, reindexed_edges = np.unique(edges, return_inverse=True)
    return reindexed_edges.reshape(edges.shape), original_ids


def extract_largest_component(edges: np.ndarray, n: int) -> tuple[np.ndarray, np.ndarray]:
    adjacency = coo_array((np.ones(len(edges)), edges.T), shape=(n, n))
    _, labels = connected_components(adjacency, directed=False)
    largest_label = np.bincount(labels).argmax()
    return reindex_vertices(edges[labels[edges[:, 0]] == largest_label])
