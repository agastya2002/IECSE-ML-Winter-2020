def is_palindrome(l):
    rl=l[::-1]
    if(rl==l):
        return True
    return False

assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False