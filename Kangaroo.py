# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 09:24:54 2017

@author: Lúcio
"""

# Take inputs
#x1,v1,x2,v2 = input().strip().split(' ')
#x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

# Testcase
#x1,v1,x2,v2 = [0, 3, 4, 2]
x1,v1,x2,v2 = [0, 2, 5, 3]

# Algorithm
ans = 'NO'
for i in range(10000):
    if x1 + v1*i == x2 + v2*i:
        ans = 'YES'
        break

print(ans)