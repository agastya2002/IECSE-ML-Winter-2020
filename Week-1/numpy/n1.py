import numpy as np
 
def gen_strides(a, stride_len, window_len):
	print(a[:window_len])
	print(a[stride_len:window_len+stride_len])
	print(a[2*stride_len:window_len+2*stride_len])
 
 
arr=np.array([1, 3, 7, 1, 2, 6, 0, 1])
 
gen_strides(arr,2,3)