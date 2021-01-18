def compress(l):
    length = len(l)
    for x in range(0,length-1):
        if(l[x]==l[x+1]):
            l[x]=' '
    newlist=[]        
    for x in range(0,length):
        if(l[x]!=' '):
            newlist.append(l[x])
    return newlist

assert(compress([1, 2, 2])) == [1, 2]
assert(compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])) == [1, 2, 1, 3, 'x']  