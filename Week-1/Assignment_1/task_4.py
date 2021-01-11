def is_palindrome(l):
    """
    Returns True if l is a palindrome, False otherwise
    """
    return (l==l[::-1])

"""Testing code for is_palindrome"""

assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False