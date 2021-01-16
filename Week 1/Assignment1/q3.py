def reverse_list(l):
    l.reverse()
    return l
n=int(input("Enter length of list: "))
l=[]
i=0
while i<n:
    x=int(input("Enter element: "))
    l.append(x)
    i=i+1
print(reverse_list(l))
