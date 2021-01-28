# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:27:44 2021

@author: home
"""
import numpy as np
def gen_strides(a, stride_len, window_len):
    '''
    Input:
      a: Numpy array of 1 dimension
      stride_len: int, stride length
      window_len: int, window length
    
    Output:
      Numpy array of 2 dimensions containing windowed strides as explained above
    '''
    # YOUR CODE HERE
    elements=[]
    for i in range(0,(len(a)+1-window_len),stride_len):
        for j in range(window_len):
            elements.append(a[i+j])
    matrix=np.array(elements).reshape((len(elements)//window_len),window_len)
    return matrix
    
"""Test for strides"""
assert (np.all(gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]),2,4) == np.array([[1, 3, 7, 1], [7, 1, 2, 6], [2, 6, 0, 1]])))

print("Sample Tests passed", '\U0001F44D')