def compress(l):
    i=1
    j=[l[0]]
    while(i<len(l)-1):
        if(l[i]==l[i-1]):
            i=i+1
            continue

        j.append(l[i])
        i=i+1

    return j
l = ['a', 'a', 'b', 'b', 'c', 'a', 'a', 'd', 'd', 'd']
print(compress(l))