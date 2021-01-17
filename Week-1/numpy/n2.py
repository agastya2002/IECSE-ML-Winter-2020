import numpy as np
 
def shuf(a):
	np.random.shuffle(a)
	return a
 
arr=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(shuf(arr))