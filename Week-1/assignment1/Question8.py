# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:20:33 2021

@author: Aarushi
"""

def insert_element(l, i, elem):
      l.insert(i,elem)
      return l

print(insert_element([1, 5], 3, 5))
print(insert_element([1, 2, 3, 4,], 2, 5)[2]) 