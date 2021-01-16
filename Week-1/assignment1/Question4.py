# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:01:51 2021

@author: Aarushi
"""

def is_palindrome(l):
   
    return l==l[::-1]  
    

print(is_palindrome([1, 2, 1]))
print(is_palindrome([1, 2, 3, 2, 1]))
print(is_palindrome([1, 2, 3, 1]))
