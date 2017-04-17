# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:28:36 2017

@author: Lúcio
"""

#!/bin/python3

import sys


n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))

#n = 3
#calories = [1, 3, 2]

calories.sort(reverse=True)

miles = 0
for i in range(len(calories)):
    miles += calories[i]*(2**i)

print(miles)