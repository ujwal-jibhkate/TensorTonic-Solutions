import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    # Write code here
    v = np.asarray(v, dtype=float)
    w = np.asarray(w, dtype=float)

    v_norm = np.sqrt(np.sum(np.square(v)))
    w_norm = np.sqrt(np.sum(np.square(w)))

    if v_norm == 0 or w_norm == 0:
        return float("nan")

    c = (np.sum(v * w)) / (v_norm * w_norm)
    theta = np.arccos(c)

    return float(theta)