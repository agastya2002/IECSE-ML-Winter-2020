def lin_eqn(a,b):
    import numpy as np
    return np.dot(np.linalg.inv(a),b)

import numpy as np
x=lin_eqn(np.array([[1.0, 2.0], [3, 4]]),np.array([8.0,  18.0]))
print(x)

assert np.any(lin_eqn(np.array([[1, 2], [3, 4]]),np.array([8, 18])) == np.array([2., 3.]))
print("Sample Tests passed", '\U0001F44D')