def last_element(l):
    return l[-1]


n=int(input("Enter length of list"))
l=[]
i=0
while(i<n):
    x=int(input("Enter element"))
    l.append(x)
    i=i+1
print(last_element(l))
