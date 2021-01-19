def rankArray(arr):
    import numpy as np
    return arr.argsort(axis=None).argsort().reshape(arr.shape)


import numpy as np
print(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])).tolist())

assert np.all(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])) == np.array([[4,2, 6, 0, 8], [7, 9, 3, 5, 1]]).tolist())
print("Sample Tests passed", '\U0001F44D')

