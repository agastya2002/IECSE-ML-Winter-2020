
def compress(l):
    i=1
    m=[l[0]]
    while(i<len(l)-1):
        if(l[i]==l[i-1]):
            i=i+1
            continue;

        m.append(l[i])
        i=i+1

    return m

l = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a', 'd', 'd', 'd', 'x', 'x']
print(compress(l))
