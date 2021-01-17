def insert_element(l, i, elem):
    """
    Returns a new list containing elem at index i. If i > len (l), insert element at the end of the list
    """
    # YOUR CODE HERE
    j=0
    l.append(0)
    if(i<len(l)-1):
        for j in range(len(l)-1,i,-1):
            l[j]=l[j-1]
        l[i]=elem

    else:
        l[len(l)-1]=elem

    return l
l = [1, 3, 9, 8, 7]
print(insert_element(l, 1, 3))