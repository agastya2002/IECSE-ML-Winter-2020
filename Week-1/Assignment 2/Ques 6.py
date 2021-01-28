# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:05:31 2021

@author: home
"""
import numpy as np

def rankArray(arr):
    '''
    Input:
        arr: Numpy array of arbitrary dimensions 
    Output:
        numpy array of same shape as arr but with elements replaced by their ranks
    '''
    #YOUR CODE HERE
    x = np.argsort(arr,axis=None)
    rank = np.argsort(x).reshape(arr.shape)
    return rank
   

"""Test for rankArray"""
assert np.all(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])) == np.array([[4,2, 6, 0, 8], [7, 9, 3, 5, 1]]).tolist())
print("Sample Tests passed", '\U0001F44D')
