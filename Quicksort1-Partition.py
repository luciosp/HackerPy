# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:38:20 2017

@author: Lúcio
"""

#Algorithm
def quicksort(l):
    left = []
    equal = []
    right = []
    p = l[0]
    for x in l:
        if x > p:
            right.append(x)
        elif x == p:
            equal.append(x)
        else:
            left.append(x)
    s = ' '.join(map(str, left + equal + right))
    return s

# Take inputs
#m = int(input().strip())
#ar = [int(i) for i in input().strip().split()]

# Testcases
size = 5
ar = [4, 5, 3, 7, 2]

print(quicksort(ar))