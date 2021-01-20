import numpy as np
#windows and strides
def gen_strides(a, stride_len, window_len):
    '''
    Input:
      a: Numpy array of 1 dimension
      stride_len: int, stride length
      window_len : int, window length
    
    Output:
      Numpy array of 2 dimensions containing windowed strides as explained above
    '''
    #shape of 2d array: (total length/stride length) - 1 by window_len
    return_list = []
    temp_list = []
    a_list = a.tolist()
    len_array = len(a_list)
    rows = (len_array/stride_len) - 1
    j = 0
    for i in range(0,int(rows)):
        if j > len_array:
            break
        temp_list = a_list[j:j+window_len]
        return_list.append(temp_list)
        j += stride_len
    return_array = np.array(return_list)
    return return_array  


    
"""Test for strides"""
assert (np.all(gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]),2,4) == 
np.array([[1, 3, 7, 1], [7, 1, 2, 6], [2, 6, 0, 1]])))

print("Sample Tests passed", '\U0001F44D')