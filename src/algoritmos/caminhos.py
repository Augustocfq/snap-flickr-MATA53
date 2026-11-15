import heapq
import math


def build_weighted_adjacency(
    n: int, edges: list[tuple[int, int, int]]
) -> list[list[tuple[int, int]]]:
    adjacency = [[] for _ in range(n)]
    for u, v, weight in edges:
        adjacency[u].append((v, weight))
        adjacency[v].append((u, weight))
    return adjacency


def dijkstra(adjacency: list[list[tuple[int, int]]], source: int) -> list[float]:
    distances = [math.inf] * len(adjacency)
    distances[source] = 0
    heap = [(0, source)]
    while heap:
        distance, u = heapq.heappop(heap)
        if distance > distances[u]:
            continue
        for v, weight in adjacency[u]:
            if distance + weight < distances[v]:
                distances[v] = distance + weight
                heapq.heappush(heap, (distances[v], v))
    return distances


def bellman_ford(
    adjacency: list[list[tuple[int, int]]], source: int
) -> tuple[list[float], int]:
    distances = [math.inf] * len(adjacency)
    distances[source] = 0
    for rounds in range(1, len(adjacency)):
        has_changed = False
        for u, neighbors in enumerate(adjacency):
            for v, weight in neighbors:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    has_changed = True
        if not has_changed:
            return distances, rounds
    return distances, len(adjacency) - 1
