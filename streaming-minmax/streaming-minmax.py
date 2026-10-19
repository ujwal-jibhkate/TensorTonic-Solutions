import numpy as np

def streaming_minmax(D: int, batches: list, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with normalized_batches, min, and max.
    """
    
    m = np.full(D, np.inf)
    M = np.full(D, -np.inf)

    normalized_batches = []

    for batch in batches:
        local_m = np.min(batch, axis = 0)
        local_M = np.max(batch, axis = 0)

        m = np.minimum(m, local_m)
        M = np.maximum(M, local_M)

        denominator = np.maximum(M - m , eps)
        normalized_batch = (batch - m) / denominator

        normalized_batches.append(normalized_batch)

    return {
        "normalized_batches" : normalized_batches,
        "min" : m,
        "max" : M
    }