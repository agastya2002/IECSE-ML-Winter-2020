def pack(l):
    """
    Returns a list with consecutive duplicate elements packed into sublists
    """
    # YOUR CODE HERE
    l1=[]
    l1.append(l[0])
    l2=[]
    for i in range (1,len(l)):
        if l[i]==l[i-1]:
            l1.append(l[i])            
        else:  
            l2.append(l1)            
            l1=[]
            l1.append(l[i])
            
            
    l2.append(l1)              
    return l2        
"""Testing code for pack"""
assert(pack([1, 1, 1, 2]) == [[1, 1, 1], [2]])
assert(pack([1, 1, 1, 2, 1, 1, 3, 3, 3])) == [[1, 1, 1], [2], [1, 1], [3, 3, 3]]