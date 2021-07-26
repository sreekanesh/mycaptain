# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:22:45 2021

@author: sreekanesh
"""
lst=[]

n=int(input('enter the number of elements :'))


for i in range(0,n):
    elements=(int(input()))
    lst.append(elements)
    
    

def positive_num():
    for item in lst:
        if item < 0:
            lst.remove(item)
            print(lst)
            
            
positive_num()            