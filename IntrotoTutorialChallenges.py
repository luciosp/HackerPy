# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 07:42:23 2017

@author: Lúcio
"""

# Take inputs
v = int(input().strip())
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))


# Testcases
#v = 4
#n = 6
#ar = [1, 4, 5, 7, 9, 12]


#Algorithm
for i in range(len(ar)):
    if ar[i] == v:
        print(i)
    