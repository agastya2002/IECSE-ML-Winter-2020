def is_palindrome(l):
    """
    Returns True if l is a palindrome, False otherwise
    """
    rev_l = []
    i = len(l)-1
    while i >= 0:
        rev_l.append(l[i])
        i -= 1
    if l == rev_l:
        return True
    else:
        return False    

    


assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False