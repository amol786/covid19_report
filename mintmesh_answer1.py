# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 21:42:41 2021

@author: 014902
"""
#Method 1
#using combination in array for subsequence  
from itertools import combinations 

def print_powerset(arr):
    
    count =0
    
    for i in range(0,len(arr)+1):
        for ele in combinations(arr,i):
            print(ele)
            if len(ele) ==2 and sum(ele) <=1000:
                count+=1
    
    return count
arr=[1,2,8]
#arr = [5,17,1000,11]
print(print_powerset(arr))