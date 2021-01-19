def pack(l):
    """
    Returns a list with consecutive duplicate elements packed into sublists
    """
    from itertools import groupby
    a = []
    for key, group in groupby(l):
        a.append(list(group))

    return a

assert(pack([1, 1, 1, 2]) == [[1, 1, 1], [2]])
assert(pack([1, 1, 1, 2, 1, 1, 3, 3, 3])) == [[1, 1, 1], [2], [1, 1], [3, 3, 3]]