import numpy as np

def lin_eqn(a,b):
  return (np.dot(np.linalg.inv(a),b))

"""Test for lin_eqn"""
assert np.any(lin_eqn(np.array([[1, 2], [3, 4]]),np.array([8, 18])) == np.array([2., 3.]))

print("Sample Tests passed", '\U0001F44D')
