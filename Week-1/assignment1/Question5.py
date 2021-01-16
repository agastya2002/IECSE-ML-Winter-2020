# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:07:45 2021

@author: Aarushi
"""

def compress(l):
   
    i=1
    while i<len(l):
        
        if l[i-1]==l[i]:
            l.pop(i)
        else:
            i+=1
        
    return l
    
 
l = ['a', 'a', 'a', 'b', 'b', 'c', 'a', 'a', 'd', 'd', 'd', 'x', 'x']
print(compress(l))
