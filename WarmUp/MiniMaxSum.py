# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:52:58 2017

@author: Lúcio
"""

#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

vector = [a,b,c,d,e]

outElement = 0
sumVector = []

for i in range(len(vector)):
    currentSum = 0
    for j in range(len(vector)):
        if j != outElement:
            currentSum += vector[j]
    outElement += 1
    sumVector.append(currentSum)

print(str(min(sumVector)) + ' ' + str(max(sumVector)))
