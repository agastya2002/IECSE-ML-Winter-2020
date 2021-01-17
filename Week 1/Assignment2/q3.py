import numpy as np

def match(a,b):
    l=len(a)
    i=0
    m=[]
    for i in range (l):
        if(a[i]==b[i]):
            m.append(i)
    return m
    
assert(match(np.array([1,2,3,2,3,4,3,4,5,6]),np.array([7,2,10,2,7,4,9,4,9,8])) == [1,3,5,7])
print("Sample Tests passed", '\U0001F44D')