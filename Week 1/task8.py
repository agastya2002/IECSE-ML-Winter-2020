def insert_element(l, i, elem):
    """
    Returns a new list containing elem at index i. If i > len (l), insert element at the end of the list
    """

    k= len(l)
    if k > i :
        l.insert(i,elem)
    else:
        l.append(elem)
    return l
        

"""Testing code for insert_element"""
assert(insert_element([1, 2, 3, 4,], 2, 5)[2]) == 5
assert(insert_element([1, 5, ], 3, 5)) == [1, 5, 5]
