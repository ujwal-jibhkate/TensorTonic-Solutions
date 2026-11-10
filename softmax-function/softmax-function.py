import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    x = np.asarray(x, dtype=float)
    
    if x.ndim == 1:
      m = np.max(x)
    else:
      m = np.max(x, axis=1, keepdims=True)
    
    x = x - m
    x = np.exp(x)
    if x.ndim == 1:
        sum = np.sum(x)
    else:
        sum = np.sum(x, axis=1, keepdims=True)

    return x/sum