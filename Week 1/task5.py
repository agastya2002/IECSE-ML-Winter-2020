def compress(l):
    """
    Returns a list with consecutive duplicate elements replaced by a single element
    """
    
    i = 0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            del l[i]
        else:
            i+=1
    return l
    
        
      
      
"""Testing code for compress"""

assert(compress([1, 2, 2])) == [1, 2]
assert(compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])) == [1, 2, 1, 3, 'x']
