# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 09:58:19 2017

@author: Lúcio
"""

# Take inputs
#n,m = input().strip().split(' ')
#n,m = [int(n),int(m)]
#a = [int(a_temp) for a_temp in input().strip().split(' ')]
#b = [int(b_temp) for b_temp in input().strip().split(' ')]

# Testcases
n,m = [2, 3]
a = [2, 4]
b = [16, 32, 96]

# Algorithm
x = []
for i in range(min(a), max(b) + 1):
    tempB = [f for f in b if f%i == 0]
    if tempB == b:
        tempA = [1 for f in a if i%f == 0]
        if len(tempA) == len(a):
            x.append(i)

print(len(x))

    