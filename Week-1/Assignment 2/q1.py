import numpy as np

def gen_strides(a, stride_len, window_len):
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

print(gen_strides(np.array([1, 3, 7, 1, 2, 6, 0, 1]),2,4))