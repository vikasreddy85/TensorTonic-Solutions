from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    mean = np.mean(x)
    med = np.median(x)
    vals, counts = np.unique(x, return_counts=True)
    mode = vals[counts.argmax()]
    return {"mean": float(mean), "median": float(med), "mode": float(mode)}
    pass