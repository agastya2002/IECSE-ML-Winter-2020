import numpy as np

def shuf(arr):
    

    for i in range(len(arr)):
        b=i
        while(b==i):
            b=np.random.randint(0,len(arr)) ## b is a random row index
   
        for j in range(len(arr[i])):
            t=arr[i][j]
            arr[i][j]=arr[b][j]
            arr[b][j]=t
    return arr


a=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(shuf(a))
