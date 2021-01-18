def insert_element(l,i,elem):
    if(i>=len(l)):
        l.append(elem)
    else:
        l.insert(i,elem)
    return l

assert(insert_element([1, 2, 3, 4,], 2, 5)[2]) == 5
assert(insert_element([1, 5], 3, 5)) == [1, 5, 5]  