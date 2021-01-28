import numpy as np
def match(a,b):
    '''
    Inputs:
      a, b: numpy arrays of same shape of 1 dimension
    Outputs:
      list containing indices where both arrays have same elements
    '''
    # YOUR CODE HERE
    ele=[]
    small=min(len(a),len(b))
    for i in range (small):
        if a[i]==b[i]:
            ele.append(i)
    return ele        
"""Test for match"""
assert(match(np.array([1,2,3,2,3,4,3,4,5,6]),np.array([7,2,10,2,7,4,9,4,9,8])) == [1,3,5,7])
print("Sample Tests passed", '\U0001F44D')

