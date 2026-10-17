import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    C = np.asarray(C, dtype=float)
    row_sums = C.sum(axis=1, keepdims=True)
    col_sums = C.sum(axis=0, keepdims=True)
    grand_total = C.sum()

    expected = (row_sums * col_sums) / grand_total

    chi2_stat = np.sum((C - expected) ** 2 / expected)

    return {
        "chi2" : float(chi2_stat),
        "expected" : expected
    }