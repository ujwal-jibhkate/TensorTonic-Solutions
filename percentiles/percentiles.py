import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    x = np.asarray(x, dtype=float)
    q = np.asarray(q, dtype=float)
    result = []
    x.sort()
    n = x.size

    for i in q:
        r = (i/100) * (n - 1)
        l = np.floor(r).astype(int)
        u = np.ceil(r).astype(int)
        w = r - l
        result.append((1-w)*x[l] + w*x[u])

    return np.asarray(result)