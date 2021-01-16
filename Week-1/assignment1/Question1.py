# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:19:27 2021

@author: Aarushi
"""

##### Question 1
def last_element(l):
    
     return l[-1]
     
         
n=int(input("Enter length of list"))
lst=[]
i=0
while i<n:
    x=int(input("Enter element"))
    lst.append(x)
    
    i+=1
print(last_element(lst)) 
     


     