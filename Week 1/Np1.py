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
    y = ((a.size-window_len)//stride_len)+1
    x= a[stride_len*np.arange(y)[:,None] + np.arange(window_len)]
    return x

assert (np.all(gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]),2,4) == np.array([[1, 3, 7, 1], [7, 1, 2, 6], [2, 6, 0, 1]])))

print("Sample Tests passed", '\U0001F44D')
