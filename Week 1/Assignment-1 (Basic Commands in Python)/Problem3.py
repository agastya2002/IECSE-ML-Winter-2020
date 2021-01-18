def reverse_list(l):
    i=0
    rl=[]
    for x in range(len(l)-1,-1,-1):
        rl.append(l[x])
        i=i+1
    return rl

assert reverse_list([2, 3, 4])== [4, 3, 2]