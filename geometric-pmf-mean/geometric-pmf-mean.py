import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    k = np.asarray(k, dtype=float)
    return {
        "pmf" : ((1.0 - p)**(k - 1)) * p,
        "mean" : float(1/p)
    }