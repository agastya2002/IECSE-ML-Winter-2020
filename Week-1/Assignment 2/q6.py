import numpy as np
def rankArray(arr):
    m=arr.tolist()
    l=len(m)
    single=[]
    for i in range(len(m)):
        for j in m[i]:
            single.append(j) #b=arr.flatten()
    unsorted=single.copy()
    single.sort()
    ans=np.zeros(len(single))
    
    for i in range(len(single)):
        for j in range(len(unsorted)):
            if(unsorted[j]==single[i]):
                ans[j]=i
                unsorted[j]="*"
                break
    
    ar=np.array(ans)
    ar=ar.reshape((l,-1))
    return ar
    """b=arr.flatten()
  sort_arr = np.sort(b)
  for ele in b:
    for i in range(len(b)):
      if sort_arr[i]==ele:
        ele=i"""



np.all(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])) == np.array([[4,2, 6, 0, 8], [7, 9, 3, 5, 1]]).tolist())
print("Sample Tests passed", '\U0001F44D')

print(rankArray(np.array([[9, 4, 15, 0, 17], [16,17,8,9,0]])).tolist())
