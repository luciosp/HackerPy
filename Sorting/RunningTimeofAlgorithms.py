# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 11:16:13 2017

@author: Lúcio
"""

def insertion_sort(l):
    count = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           count += 1
           j -= 1
        l[j+1] = key
    return count

# Take inputs
#m = int(input().strip())
#ar = [int(i) for i in input().strip().split()]

# Testcases
size = 5
ar = [2, 1, 3, 1, 2]

#Algorithm
print(insertion_sort(ar))