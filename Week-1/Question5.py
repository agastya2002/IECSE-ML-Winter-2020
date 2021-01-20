def compress(l):
    """
    Returns a list with consecutive duplicate elements replaced by a single element
    """
    # YOUR CODE HERE
    return_list = []
    return_list.append(l[0])
    for element in l[1:]:
        return_list.append(element)
        if element == return_list[-2]:
            return_list  = return_list[:-1]
    return return_list
print(compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x']))      
print(compress([1, 2, 2]))
assert(compress([1, 2, 2])) == [1, 2]
assert(compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])) == [1, 2, 1, 3, 'x']
