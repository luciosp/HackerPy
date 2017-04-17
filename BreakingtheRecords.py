# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:33:04 2017

@author: Lúcio
"""

#!/bin/python3

import sys

def getRecord(s):
    high = s[0]
    low = s[0]
    count = [0, 0]
    for score in s[1:len(s)+1]:
        if score > high:
            count[0] += 1
            high = score
        
        if score < low:
            count[1] += 1
            low = score
    return count
        

#n = int(input().strip())
#s = list(map(int, input().strip().split(' ')))
n = 9
s = [10, 5, 20, 20, 4, 5, 2, 25, 1]
result = getRecord(s)
print (" ".join(map(str, result)))