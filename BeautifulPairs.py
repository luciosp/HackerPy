# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:12:47 2017

@author: Lúcio
"""

# Take inputs
#n = int(input().strip())
#a = list(map(int, input().strip().split(' ')))
#b = list(map(int, input().strip().split(' ')))

# Testcases
n = 3
a = [1, 2, 2]
b = [1, 2, 3]

# Algorithm
# Find beautiflu pairs
beautifulPairs = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            beautifulPairs.append([i, j])
            
print(beautifulPairs)