
import numpy as np
def lin_eqn(a,b):
    '''
    Solve the system of linear equations
    of the form ax = b
    
    Eg. 
    
    Solve the system of linear equation
    
    x + 2*y = 8
    3*x + 4*y = 18
    
    Given inputs a and b represent coefficients and constant of linear equation respectively
    
    coefficients: 
    a = np.array([[1, 2], [3, 4]]) 
    
    constants: 
    b = np.array([8, 18])
    
    Desired Output: [2,3]
    

    '''
    # YOUR CODE HERE
    sol=np.linalg.inv(a).dot(b)
    return(sol)
x=lin_eqn(np.array([[1.0, 2.0], [3, 4]]),np.array([8.0,  18.0]))
print(x)
"""Test for lin_eqn"""
assert np.any(lin_eqn(np.array([[1, 2], [3, 4]]),np.array([8, 18])) == np.array([2., 3.]))

print("Sample Tests passed", '\U0001F44D')