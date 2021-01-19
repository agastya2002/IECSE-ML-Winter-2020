def inv(arr):
    """
    Given an array arr (square matrix), find its inverse
    """
    return np.linalg.inv(arr)

"""Test for inv"""
import numpy as np
assert np.all(np.isclose(inv(np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])).tolist(), np.array(
    [[0.17647058823529413, -0.0032679738562091526, -0.02287581699346405],
     [0.05882352941176469, -0.130718954248366, 0.0849673202614379],[-0.1176470588235294, 0.1503267973856209, 0.0522875816993464]])))

print("Sample Tests passed", '\U0001F44D')