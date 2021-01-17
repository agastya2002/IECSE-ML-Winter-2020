def pack(l):
    i=0
    j=0
    k=0
    p=[]
    q=[]
    while(i<len(l)) :
        a=l[i]
        k=0

        while(l[i]==a) :
            i+=1
            k+=1
            if(i==len(l)) :
                break

        j=0
        for j in range(k) :
            q.append(a)

        p.append(q)
        q=[]

    return p


print(pack([1, 1, 1, 2, 2, 3, 3, 4]))