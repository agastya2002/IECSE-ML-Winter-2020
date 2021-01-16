def compress(l):
    res = [] 
    for i in l: 
        if i not in res: 
            res.append(i)
    return res


n=int(input("Enter length of list: "))
l=[]
i=0
while i<n:
    x=int(input("Enter element: "))
    l.append(x)
    i=i+1
print(compress(l))