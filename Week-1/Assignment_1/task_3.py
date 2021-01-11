def reverse_list(l):
    """
    Returns the reverse of a list l
    """
    return l[::-1]
l = [1, 2, 3, 4]
print(reverse_list(l))

"""Testing code for reverse_list"""
assert reverse_list([2, 3, 4])== [4, 3, 2]