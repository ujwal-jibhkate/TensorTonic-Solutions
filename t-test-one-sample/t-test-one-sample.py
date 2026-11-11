import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x = np.asarray(x, dtype=float)
    n = x.size
    mean = np.mean(x)
    centered = x - mean
    sum = np.sum(np.square(centered))
    s = np.sqrt(sum/(n-1))

    t = (mean - mu0)/(s/np.sqrt(n))

    return float(t)