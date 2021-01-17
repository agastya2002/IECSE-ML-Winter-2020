import numpy as np
 
def match(a,b):
	print(np.where(a==b))
 
x = np.array([1,2,3,2,3,4,3,4,5,6]) 
y = np.array([7,2,10,2,7,4,9,4,9,8]) 
 
match(x,y)