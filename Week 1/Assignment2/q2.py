import numpy as np

def shuf(arr):
    for i in range(len(arr)):
        b=np.random.randint(0,len(arr))
        while b==i:
            b=np.random.randint(0,len(arr))  ##b is a random row index
        for j in range(len(arr[i])):
            t=arr[i][j]
            arr[i][j]=arr[b][j]
            arr[b][j]=t
    ##np.random.shuffle(arr)
    return arr


a=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(shuf(a))

assert np.any(shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])) != np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
assert shuf(np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])).shape == np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).shape
print("Sample Tests passed", '\U0001F44D')