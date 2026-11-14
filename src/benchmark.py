import time
from collections.abc import Callable

import numpy as np
from scipy import stats


def summarize_times(algorithm: str, entry: str, times: list[float]) -> dict:
    r = len(times)
    mean = np.mean(times)
    deviation = np.std(times, ddof=1)
    if r >= 30:
        distribution, critical_value = "Z", stats.norm.ppf(0.975)
    else:
        distribution, critical_value = "t", stats.t.ppf(0.975, r - 1)
    margin = critical_value * deviation / np.sqrt(r)
    return {
        "algorithm": algorithm,
        "input": entry,
        "repetitions": r,
        "mean": mean,
        "deviation": deviation,
        "ci_lower": mean - margin,
        "ci_upper": mean + margin,
        "distribution": distribution,
    }


def measure_time(algorithm: str, entry: str, run: Callable[[], object], repetitions: int) -> dict:
    run()
    times = []
    for _ in range(repetitions):
        start = time.perf_counter()
        run()
        times.append(time.perf_counter() - start)
    return summarize_times(algorithm, entry, times)
