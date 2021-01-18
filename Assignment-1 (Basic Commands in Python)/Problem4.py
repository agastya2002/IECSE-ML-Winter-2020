def is_palindrome(l):
    rl=[]
    length=len(l)
    for x in range(length-1,-1,-1):
        rl.append(l[x])
    if(rl==l):
        return True
    return False

assert(is_palindrome([1, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 2, 1])) == True
assert(is_palindrome([1, 2, 3, 4])) == False