import numpy as np


def fit_tail(k: np.ndarray, frequency: np.ndarray, k_min: int) -> tuple[float, float]:
    tail_k, tail_frequency = k[k >= k_min], frequency[k >= k_min]
    tail_size = tail_frequency.sum()
    alpha = 1 + tail_size / np.sum(tail_frequency * np.log(tail_k / (k_min - 0.5)))
    empirical_ccdf = tail_frequency[::-1].cumsum()[::-1] / tail_size
    fitted_ccdf = ((tail_k - 0.5) / (k_min - 0.5)) ** (1 - alpha)
    return alpha, np.abs(empirical_ccdf - fitted_ccdf).max()


def fit_power_law(k: np.ndarray, frequency: np.ndarray) -> tuple[int, float, float]:
    fits = [(int(k_min), *fit_tail(k, frequency, k_min)) for k_min in k[:-1]]
    return min(fits, key=lambda fit: fit[2])
