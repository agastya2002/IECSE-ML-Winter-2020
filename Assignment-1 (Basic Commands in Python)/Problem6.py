def pack(l):
    count=0
    print(l)
    l.append('.')
    length=len(l)
    rl=[]
    nl=[]
    for x in range(1,length):
        if(l[x]==l[x-1]):
            count=count+1
        else:
            for y in range(x-1-count,x):
                nl.append(l[y])
            rl.append(nl)
            nl=[]
            count=0
    return rl

assert(pack([1, 1, 1, 2]) == [[1, 1, 1], [2]])
assert(pack([1, 1, 1, 2, 1, 1, 3, 3, 3])) == [[1, 1, 1], [2], [1, 1], [3, 3, 3]]