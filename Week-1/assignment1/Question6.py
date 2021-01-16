# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:38:10 2021

@author: Aarushi
"""

def pack(l):
    i=0
    j=0
    k=0
    n=[]
    z=[]
    while(i<len(l)) :
        a=l[i]
        k=0

        while(l[i]==a) :
            i+=1
            k+=1
            if(i==len(l)) :
                break

        j=0
        for j in range(k) :
            z.append(a)

        n.append(z)
        z=[]

    return n


print(pack([1, 1, 1, 2, 2, 3, 3, 4]))
