
def is_palindrome(l):
    return l==l[::-1]

print(is_palindrome([1, 2, 1]))
print(is_palindrome([1, 2, 3, 2, 1]))
print(is_palindrome([1, 2, 3, 1]))
