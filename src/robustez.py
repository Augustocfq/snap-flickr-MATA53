import numpy as np
from scipy.sparse import csr_array
from scipy.sparse.csgraph import connected_components, shortest_path


def measure_robustness_metrics(
    n: int, edges: np.ndarray, removed: np.ndarray, sources_count: int, rng: np.random.Generator
) -> tuple[float, int, float, float]:
    is_kept = np.ones(n, dtype=bool)
    is_kept[removed] = False
    kept_edges = edges[is_kept[edges].all(axis=1)]
    graph = csr_array((np.ones(len(kept_edges)), (kept_edges[:, 0], kept_edges[:, 1])), shape=(n, n))
    labels = connected_components(graph, directed=False)[1]
    component_sizes = np.bincount(labels[is_kept])
    largest_size = component_sizes.max()
    is_in_largest = labels == component_sizes.argmax()
    sources = rng.choice(np.flatnonzero(is_in_largest), size=sources_count, replace=False)
    distances = shortest_path(graph, directed=False, unweighted=True, indices=sources)
    return (
        largest_size / n,
        np.count_nonzero(component_sizes),
        (distances[:, is_in_largest].sum(axis=1) / (largest_size - 1)).mean(),
        np.count_nonzero(component_sizes == 1) / is_kept.sum(),
    )
