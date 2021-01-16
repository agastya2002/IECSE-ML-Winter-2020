def pack(l):
    i,j,k=0,0,0
    m=[]
    b=[]
    while(i<len(l)) :
        a=l[i]
        k=0
        while(l[i]==a) :
            i+=1
            k+=1
            if(i==len(l)):
                break
        j=0
        for j in range(k) :
            b.append(a)
        m.append(b)
        b=[]
    return m

n=int(input("Enter length of list: "))
l=[]
i=0
while i<n:
    x=int(input("Enter element: "))
    l.append(x)
    i=i+1
print(pack(l))