import numpy as np
def rankArray(arr):
    li=list(np.sort(arr.flatten()))
    for i in range(0,arr.shape[0]):
        for j in range(0,arr.shape[1]):
            for h in range(0,len(li)):
                if(arr[i][j]==li[h]):
                    arr[i][j]=h
                    li[h]="#"
                    break
    return arr
    


def rankArraytry1(given_list):
    
    merged_list = []
    for i in given_list:
        for j in i:
            merged_list.append(j)
    merged_ranklist = ranks(merged_list)
    count = 0
    final_rankedlist = []
    elemental_rankedlist = []
    i=0
    for element in range(0, len(merged_ranklist)):
        elemental_rankedlist.append(merged_ranklist[element])
        count+=1
        if(count == len(given_list[i])):
            i+=1
            count = 0
            final_rankedlist.append(elemental_rankedlist)
            elemental_rankedlist = []
    return np.array(final_rankedlist) 



        






print(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])).tolist())
[[4, 2, 6, 0, 8], [7, 9, 3, 5, 1]]
print(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])))
"""Test for rankArray"""
assert np.all(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])) == np.array([[4,2, 6, 0, 8], [7, 9, 3, 5, 1]]).tolist())

print("Sample Tests passed", '\U0001F44D')