from src.algoritmos.buscas import depth_first_search


def check_eulerian(adjacency: list[list[int]]) -> dict:
    odd_degree_vertices = sum(len(neighbors) % 2 for neighbors in adjacency)
    is_connected = len(depth_first_search(adjacency, 0)) == len(adjacency)
    return {
        "odd_degree_vertices": odd_degree_vertices,
        "is_connected": is_connected,
        "has_eulerian_circuit": is_connected and odd_degree_vertices == 0,
        "has_eulerian_path": is_connected and odd_degree_vertices == 2,
    }
