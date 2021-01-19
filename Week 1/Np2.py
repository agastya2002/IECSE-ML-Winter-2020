def shuf(arr):
  '''
  Input:
    arr: Numpy array of arbitrary number of dimensions (>1)
  Output:
    numpy array of same shape as arr but with rows shuffled
  '''
  import numpy as np
  np.random.shuffle(arr)
  print(arr)
  return arr

"""Test for shuf"""
import numpy as np

arr=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
assert np.any(shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])) != np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
assert shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])).shape == np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).shape

print("Sample Tests passed", '\U0001F44D')