# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:09:18 2017

@author: Lúcio
"""

#!/bin/python3

import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

#n = 3
#a = [3, -7, 0]

a.sort();
absDiff = abs(a[0] - a[1])
for i in range(len(a)-1):
    #print(str(a[i]) + ' ' + str(a[j]))
    curAbsDiff = abs(a[i] - a[i+1])
    if curAbsDiff < absDiff:
        absDiff = curAbsDiff
    #print(str(absDiff))
        
print(str(absDiff))