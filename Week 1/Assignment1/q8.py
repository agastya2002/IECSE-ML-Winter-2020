def insert_element(l, i, elem):
    """
    Returns a new list containing elem at index i. If i > len (l), insert element at the end of the list
    """  
    a=len(l)
    if i>=a:
        l.append(elem)
    else:
        l.insert(i,elem)
    return l 

n=int(input("Enter length of list: "))
l=[]
i=0
while i<n:
    x=int(input("Enter element: "))
    l.append(x)
    i=i+1
elem=input("Enter element to be added: ")
i=int(input("Enter index: "))
print(insert_element(l, i, elem))