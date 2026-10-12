from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    results = {}
    counts = Counter(x)   
    x = np.asarray(x)
    # Mean
    results["mean"] = float(np.mean(x))
    # Median
    results["median"] = float(np.median(x))
    # Mode
    results["mode"] = float(max(counts.keys(), key=lambda k: (counts[k], -k)))
    return results