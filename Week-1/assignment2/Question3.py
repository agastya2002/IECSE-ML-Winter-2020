# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:18:53 2021

@author: Aarushi
"""
import numpy as np
def match(a,b):
    '''
    Inputs:
      a, b: numpy arrays of same shape of 1 dimension
    Outputs:
      list containing indices where both arrays have same elements
    '''
    # YOUR CODE HERE
    l=[]
    for i in range(len(a)):
        if a[i]==b[i]:
            l.append(i)
    return l
assert(match(np.array([1,2,3,2,3,4,3,4,5,6]),np.array([7,2,10,2,7,4,9,4,9,8])) == [1,3,5,7])
print("Sample Tests passed", '\U0001F44D')        