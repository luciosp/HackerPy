# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 07:54:46 2017

@author: Lúcio
"""

# Take inputs
#size = int(input().strip())
#arr = list(map(int, input().strip().split(' ')))


# Testcases
size = 5
arr = [-2, 4, 6, 7, -3]


#Algorithm
i = len(arr) - 1
e = arr[i];
while (i >= 1 and arr[i-1] > e):
    arr[i] = arr[i-1];
    i = i - 1
    print(' '.join(map(str,arr)))
    
arr[i] = e;
print(' '.join(map(str,arr)))