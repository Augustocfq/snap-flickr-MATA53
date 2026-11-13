import pickle
from collections.abc import Callable

from src.config import CACHE_DIR


def cached[T](name: str, compute: Callable[[], T]) -> T:
    path = CACHE_DIR / f"{name}.pkl"
    if path.exists():
        return pickle.loads(path.read_bytes())
    result = compute()
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path.write_bytes(pickle.dumps(result))
    return result
