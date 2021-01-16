def is_palindrome(l):
    return l==l[::-1]

n=int(input("Enter length of list: "))
l=[]
i=0
while i<n:
    x=int(input("Enter element: "))
    l.append(x)
    i=i+1
print(is_palindrome(l))