def pack1(l):                     #This is my first answer, the pack function is better
    """
    Returns a list with consecutive duplicate elements packed into sublists
    """
    element = []
    element.append(l[0])
    element_count = []
    element_count.append(1)
    j = 0
    for i in range(0,len(l)-1):              
        if l[i] != l[i+1]:
            j = j + 1
            element.append(l[i+1])
            element_count.append(1)
        else:
            element_count[j] = element_count[j] + 1
    return_list = []
    for i in range(0,len(element)):
        return_list.append([element[i]]*element_count[i])
    return return_list    

def pack(array):
    return_array = []
    sub_array = [array[0]]
    for i in range(1, len(array)):
        if array[i] != array[i-1]:
            return_array.append(sub_array)
            sub_array = [array[i]]
        else:
            sub_array.append(array[i])
    return_array.append(sub_array)
    return return_array


assert(pack([1, 1, 1, 2]) == [[1, 1, 1], [2]])
assert(pack([1, 1, 1, 2, 1, 1, 3, 3, 3])) == [[1, 1, 1], [2], [1, 1], [3, 3, 3]]