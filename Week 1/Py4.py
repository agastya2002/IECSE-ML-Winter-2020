def is_palindrome(l):
    """
    Returns True if l is a palindrome, False otherwise
    """
    k = len(l) -1 
    for i in range (0, k):
        if l[i]==l[k-i]:
            return True
        else:
            return False
assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False