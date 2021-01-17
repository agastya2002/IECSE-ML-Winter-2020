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
    # YOUR CODE HERE
    m=[]
    i=0

    while(i<len(a)-stride_len-1):
        b=[]
        j=0
        z=i
        for j in range(window_len):
            b.append(a[i])
            if(i<len(a)-1):
                i=i+1
            else:
                break
        m.append(b)

        i=z+stride_len


    return np.array(m)

"""Test for strides"""
assert (np.all(gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]),2,4) == np.array([[1, 3, 7, 1], [7, 1, 2, 6], [2, 6, 0, 1]])))

#print(gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]),2,4))

print("Sample Tests passed", '\U0001F44D')
