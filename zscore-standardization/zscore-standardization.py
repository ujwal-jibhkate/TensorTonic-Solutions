import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    X = np.asarray(X, dtype=float)
    X_mean = np.mean(X, axis = axis, keepdims=True)
    X_SD = np.std(X, axis = axis, keepdims=True)
    safe_sd = np.where(X_SD > eps, X_SD, 1.0)

    return (X - X_mean)/safe_sd
    