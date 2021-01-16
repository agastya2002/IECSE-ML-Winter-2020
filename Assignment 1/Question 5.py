def compress(l):
    """
    Returns a list with consecutive duplicate elements replaced by a single element
    """
    # YOUR CODE HERE
    l1=[]
    l1.append(l[0])
    for i in range (1,len(l)):
        if l[i]==l[i-1]:
            continue
        l1.append(l[i])
    return (l1)    
      
    
    
"""Testing code for compress"""

assert(compress([1, 2, 2])) == [1, 2]
assert(compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])) == [1, 2, 1, 3, 'x']
