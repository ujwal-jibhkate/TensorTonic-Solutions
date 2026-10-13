import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    x = np.asarray(x, dtype=float)
    x = np.sort(x)
    q = np.asarray(q, dtype=float)

    pos = (q / 100.0) * (x.size - 1)
    lower = np.floor(pos).astype(int)
    upper = np.ceil(pos).astype(int)
    weight =  pos - lower

    return x[lower] * (1.0 - weight) + x[upper] * weight

    