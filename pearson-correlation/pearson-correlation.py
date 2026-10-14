import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    x = np.asarray(X, dtype=float)
    centered = x - np.mean(x, axis = 0)
    cov = centered.T @ centered / (x.shape[0] - 1)
    sd = np.sqrt(np.diag(cov))
    den = np.outer(sd, sd)

    with np.errstate(divide="ignore", invalid="ignore"):
        return cov/den
    