def slice(l, i, k):
    l1=l[i:k]
    return l1

n=int(input("Enter length of list: "))
l=[]
i=0
while i<n:
    x=int(input("Enter element: "))
    l.append(x)
    i=i+1
i=int(input("Enter starting limit: "))
k=int(input("Enter ending limit: "))
print(slice(l, i, k))