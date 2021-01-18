def slice(l,i,k):
    rl=[]
    if(k>len(l)):
        k=len(l)
    for x in range(i,k):
        rl.append(l[x])
    return rl

assert(slice([1, 3, 8, 9, 7], 1, 3)) == [3,8]
assert(slice([1, 4, 6, 'x', 9, 0], 2, 10)) == [6, 'x', 9, 0]