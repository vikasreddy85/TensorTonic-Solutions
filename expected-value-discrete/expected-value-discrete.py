import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    res = 0
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)
    for i in range(len(x)):
        res += x[i] * p[i]
    return res   
    pass