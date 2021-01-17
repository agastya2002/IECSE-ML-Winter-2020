import numpy as np
def lin_eqn(a,b):
	print(np.linalg.solve(a,b))

abc = np.array([[1.0, 2.0], [3, 4]])
abcd = np.array([8.0,  18.0])

lin_eqn(abc,abcd)