def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    import numpy as np 
    data = np.asarray(data, dtype=float)
    print(data)

    min_cols = np.min(data, axis=0)
    max_cols = np.max(data, axis=0)

    denominator = max_cols - min_cols
    print(denominator)

    scaled = np.where(denominator == 0, 0.0, (data - min_cols) / denominator)

    return scaled.tolist()