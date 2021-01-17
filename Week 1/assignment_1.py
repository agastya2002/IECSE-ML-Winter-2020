from itertools import groupby


def last_element(l):
    return(l[-1])


last_element([1, 2, 3, 4])
assert last_element([1]) == 1
assert last_element(["Hello", "World"]) == "World"


def num_elements(l):
    """
    Returns number of elements in the list l
    """
    return len(l)


"""Testing code for num_elements"""
assert num_elements([2, 3, 4]) == 3


def reverse_list(l):
    """
    Returns the reverse of a list l
    """
    reversed_list = l[::-1]
    return reversed_list


"""Testing code for reverse_list"""
assert reverse_list([2, 3, 4]) == [4, 3, 2]


def is_palindrome(l):
    """
    Returns True if l is a palindrome, False otherwise
    """
    reversed_list = l[::-1]
    if reversed_list == l:
        return True
    else:
        return False


"""Testing code for is_palindrome"""

assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False


def compress(l):
    """
    Returns a list with consecutive duplicate elements replaced by a single element
    """
    new_list = l[:1]
    for x in l[1:]:
        if new_list[-1] != x:
            new_list.append(x)
    return new_list


"""Testing code for compress"""

assert(compress([1, 2, 2])) == [1, 2]
assert(compress([1, 2, 2, 2, 1, 1, 3, 'x', 'x', 'x'])) == [1, 2, 1, 3, 'x']


def pack(l):
    # YOUR CODE HERE
    ans = []
    for key, grp in groupby(l):
        ans.append(list(grp))
    return ans


assert(pack([1, 1, 1, 2]) == [[1, 1, 1], [2]])
assert(pack([1, 1, 1, 2, 1, 1, 3, 3, 3])) == [[1, 1, 1], [2], [1, 1], [3, 3, 3]]


def slice(l, i, k):
    """
    Returns a list containing the elements between i'th and k'th elements of original list l.
    """
    new_list = l[i:k]
    return new_list


"""Testing code for slice"""
assert(slice([1, 3, 8, 9, 7], 1, 3)) == [3, 8]
assert(slice([1, 4, 6, 'x', 9, 0], 2, 10)) == [6, 'x', 9, 0]


def insert_element(l, i, elem):
    """
    Returns a new list containing elem at index i. If i > len (l), insert element at the end of the list
    """
    l.insert(i, elem)
    return l


"""Testing code for insert_element"""
assert(insert_element([1, 2, 3, 4, ], 2, 5)[2]) == 5
assert(insert_element([1, 5, ], 3, 5)) == [1, 5, 5]
