import numpy as np

def rotate_around_z(points: list, theta: float) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as points.
    """
    points = np.asarray(points, dtype=float)
    cosine = np.cos(theta)
    sine = np.sin(theta)

    x = points[..., 0]
    y = points[..., 1]
    z = points[..., 2]

    return np.stack((x * cosine - y * sine, x * sine + y * cosine, z), axis=-1)