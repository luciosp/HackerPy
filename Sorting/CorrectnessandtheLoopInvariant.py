# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:16:13 2017

@author: Lúcio
"""

def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

# Take inputs
#m = int(input().strip())
#ar = [int(i) for i in input().strip().split()]

# Testcases
size = 6
arr = [1, 4, 3, 5, 6, -2]

#Algorithm
insertion_sort(arr)
print(" ".join(map(str,arr)))