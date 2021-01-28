def last_element(l):
    """
    Returns last element of list l
    """
    # YOUR CODE HERE
    return l[-1]

last_element([1, 2, 3, 4])

"""Testing code for last_element"""
assert last_element([1]) == 1
assert last_element(["Hello", "World"]) == "World"