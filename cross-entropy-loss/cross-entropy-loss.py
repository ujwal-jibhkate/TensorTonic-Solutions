import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    y_pred = np.asarray(y_pred, dtype=float)
    rows = np.arange(len(y_true))
    correct_probs = y_pred[rows, y_true]
    print(correct_probs)
    neg_log_probs = -np.log(correct_probs)
    return float(np.mean(neg_log_probs))