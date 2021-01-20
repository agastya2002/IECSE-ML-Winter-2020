def slice(l, i, k):
    """
    Returns a list containing the elements between i'th and k'th elements of original list l.
    """  
    if k > len(l):
        k = len(l)
    return l[i:k] 
"""Testing code for slice"""
assert(slice([1, 3, 8, 9, 7], 1, 3)) == [3,8]
assert(slice([1, 4, 6, 'x', 9, 0], 2, 10)) == [6, 'x', 9, 0]