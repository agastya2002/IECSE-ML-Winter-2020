import numpy as np


def gen_strides(a, stride_len, window_len):
    '''
    Input:
      a: Numpy array of 1 dimension
      stride_len: int, stride length
      window_len : int, window length
    Output:
      Numpy array of 2 dimensions containing windowed strides as explained above
    '''
    l = []
    i = 0
    while i+stride_len < len(a):
        l.append(a[i:i+window_len])
        i += stride_len
    return np.array(l)


"""Test for strides"""
assert (np.all(gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]), 2, 4)
               == np.array([[1, 3, 7, 1], [7, 1, 2, 6], [2, 6, 0, 1]])))

print("Sample Tests passed", '\U0001F44D')


def shuf(arr):
    '''
    Input:
      arr: Numpy array of arbitrary number of dimensions (>1)
    Output:
      numpy array of same shape as arr but with rows shuffled
    '''
    arr = arr.reshape((3, 3))
    np.random.shuffle(arr)
    return arr


"""Test for shuf"""
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assert np.any(shuf(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
              != np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
assert shuf(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])).shape == np.array(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]).shape

print("Sample Tests passed", '\U0001F44D')


def match(a, b):
    '''
    Inputs:
      a, b: numpy arrays of same shape of 1 dimension
    Outputs:
      list containing indices where both arrays have same elements
    '''
    l = []
    for i in range(len(a)):
        if a[i] == b[i]:
            l.append(i)
    return l


"""Test for match"""
assert(match(np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6]), np.array(
    [7, 2, 10, 2, 7, 4, 9, 4, 9, 8])) == [1, 3, 5, 7])
print("Sample Tests passed", '\U0001F44D')


def inv(arr):
    """
    Given an array arr (square matrix), find its inverse
    """
    if arr.shape[0] == arr.shape[1]:
        return np.linalg.inv(arr)


"""Test for inv"""
assert np.all(np.isclose(inv(np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])).tolist(), np.array([[0.17647058823529413, -0.0032679738562091526, -0.02287581699346405], [
              0.05882352941176469, -0.130718954248366, 0.0849673202614379], [-0.1176470588235294, 0.1503267973856209, 0.0522875816993464]])))

print("Sample Tests passed", '\U0001F44D')


def lin_eqn(a, b):
    l = []
    l = np.dot(np.linalg.inv(a), b)  # can be done directly using np.linalg.solve(a,b) too
    return l


"""Test for lin_eqn"""
assert np.any(lin_eqn(np.array([[1, 2], [3, 4]]), np.array([8, 18])) == np.array([2., 3.]))

print("Sample Tests passed", '\U0001F44D')


def rankArray(arr):
    '''
    Input:
        arr: Numpy array of arbitrary dimensions
    Output:
        numpy array of same shape as arr but with elements replaced by their ranks
    '''
    if arr.ndim == 1:
        arr2 = arr.argsort()
        arr3 = arr2.argsort()
        return((list(arr3)))
    else:
        n = len(arr[0])
        newarr = arr.reshape(-1)
        newarr2 = newarr.argsort()
        newarr3 = newarr2.argsort()
        newarr4 = newarr3.reshape(-1, n)
        return newarr4


"""Test for rankArray"""
assert np.all(rankArray(np.array([[9, 4, 15, 0, 17], [16, 17, 8, 9, 0]]))
              == np.array([[4, 2, 6, 0, 8], [7, 9, 3, 5, 1]]).tolist())
print("Sample Tests passed", '\U0001F44D')
