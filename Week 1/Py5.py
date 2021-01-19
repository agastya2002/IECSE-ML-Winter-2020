def compress(l):
    """
    Returns a list with consecutive duplicate elements replaced by a single element
    """
    previous_value = None
    a = []

    for i in l:
        if i != previous_value:
            a.append(i)
            previous_value = i

    return a

print (compress([1, 2, 2, 2, 1, 1, 3]))
print (compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x']))