import numpy as np

def ridge_regression(X: list, y: list, lam: float) -> list:
    """
    Returns the ridge-regression weight vector.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    I = np.identity(X.shape[-1])
    w = np.linalg.inv(X.T @ X + I*lam) @ X.T @ y
    return w.tolist()