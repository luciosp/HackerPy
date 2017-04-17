# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 08:40:55 2017

@author: Lúcio
"""

from math import ceil

n = int(input().strip())
#n = 1
for _ in range(n):
    # Take inputs
    grade = int(input().strip())
    #grade = 67
    
    # Algorithm
    if grade >= 38 and (ceil(grade/5)*5) - grade < 3:
        print(ceil(grade/5)*5)
    else:
        print(grade)