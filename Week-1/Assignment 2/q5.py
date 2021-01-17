import numpy as np
def lin_eqn(a,b):
    '''
    Solve the system of linear equations
    of the form ax = b
    '''
    c=np.linalg.inv(a)
    return np.dot(c,b)


    """Test for lin_eqn"""
assert np.any(lin_eqn(np.array([[1, 2], [3, 4]]),np.array([8, 18])) == np.array([2., 3.]))

print("Sample Tests passed", '\U0001F44D')