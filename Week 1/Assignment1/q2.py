def num_elements(l):
    return len(l)
l=[]
i=True
while i==True:
    x=input("Enter elements of list or enter STOP to finish: ")
    if x=='STOP':
        i=False
        continue
    else:
        l.append(int(x))
    
print(num_elements(l))