def reverse_list(l):
    """
    Returns the reverse of a list l
    """
    rev_list = []
    i = len(l)
    while i>0:
        rev_list.append(l[i-1])
        i = i - 1
    return rev_list
    #Can also use
    #l.reverse()
    #return l


assert reverse_list([2, 3, 4])== [4, 3, 2]