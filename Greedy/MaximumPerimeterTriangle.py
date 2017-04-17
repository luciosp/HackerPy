# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:45:49 2017

@author: Lúcio
"""


# Take inputs
n = int(input().strip())
length  = sorted(list(map(int, input().strip().split(' '))))


# Testcases
#n = 5
#length = [1, 1, 1, 3, 3]

#n = 3
#length = [1, 2, 3]


# Algorithm
# Initialize variables
maxTriangle = [0, 0, 0]

# Check for non-degenerate triangles
for i in range(n - 2):
    lengthWindow = length[i:i+3]
    if lengthWindow[0] + lengthWindow[1] > lengthWindow[2]:
        maxTriangle = lengthWindow

ans = str.join(' ', [str(ele) for ele in maxTriangle])
if maxTriangle == [0, 0, 0]:
    ans = '-1'   

print(ans)