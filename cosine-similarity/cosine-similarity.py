import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    a_norm = np.sqrt(np.sum(np.square(a))) # or np.linalg.norm(a)
    b_norm = np.sqrt(np.sum(np.square(b))) # or np.linalg.norm(b)

    if a_norm == 0 or b_norm == 0:
        return float(0)

    return float(np.dot(a,b)/(a_norm*b_norm))