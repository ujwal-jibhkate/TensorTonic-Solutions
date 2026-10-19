import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    k = np.asarray(k, dtype=float)
    ones = np.ones(k.shape)
    pmf = ((ones - p)**(k - 1)) * p
    return {
        "pmf" : pmf,
        "mean" : float(1/p)
    }