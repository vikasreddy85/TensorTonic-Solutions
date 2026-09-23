import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    mean = np.mean(x)
    sume = 0
    for i in range(len(x)):
        sume += (x[i] - mean)**2
    var = float((1 / (len(x) - 1)) * sume)
    return {"variance": var, "standard_deviation": float(np.sqrt(var))}
    pass