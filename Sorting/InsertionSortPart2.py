# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 10:53:42 2017

@author: Lúcio
"""

def sortOneElement(arr):
    i = len(arr) - 1
    e = arr[i];
    while (i >= 1 and arr[i-1] > e):
        arr[i] = arr[i-1];
        i = i - 1
    arr[i] = e;
    return arr

# Take inputs
#size = int(input().strip())
#arr = list(map(int, input().strip().split(' ')))


# Testcases
size = 5
arr = [1, 4, 3, 5, 6, 2]

#Algorithm
i = 1
while i < len(arr):
    arr[0:i+1] = sortOneElement(arr[0:i+1])
    print(' '.join(map(str,arr)))
    i += 1