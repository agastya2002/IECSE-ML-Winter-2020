def is_palindrome(l):
    """
    Returns True if l is a palindrome, False otherwise
    """
    # YOUR CODE HERE
    reversed_list=l[::-1]
    if l==reversed_list:
        return True
    else:
        return False
"""Testing code for is_palindrome"""

assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False