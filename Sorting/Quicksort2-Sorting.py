# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:58:36 2017

@author: Lúcio
"""

#Algorithm
def quicksort(l):
    if len(l) <= 1:
        return l
    else:
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
        s = quicksort(left) + equal + quicksort(right)
        print(' '.join(map(str, s)))
        return s

# Take inputs
#m = int(input().strip())
#ar = [int(i) for i in input().strip().split()]

# Testcases
ar = [5, 8, 1, 3, 7, 9, 2]
quicksort(ar)