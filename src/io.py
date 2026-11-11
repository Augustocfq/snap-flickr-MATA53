import gzip
from pathlib import Path

COMMENT_PREFIX = "#"


def read_edge_list(path: Path) -> list[tuple[int, int]]:
    edges = []
    with gzip.open(path, "rt") as edge_file:
        for line in edge_file:
            if line.startswith(COMMENT_PREFIX):
                continue
            u, v = line.split()
            edges.append((int(u), int(v)))
    return edges
