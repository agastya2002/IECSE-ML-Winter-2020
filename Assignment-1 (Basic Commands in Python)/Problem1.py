def last_element(l):
    i=0
    for x in l:
        i=i+1
    return l[i-1]    

assert last_element([1]) == 1
assert last_element(["Hello", "World"]) == "World"