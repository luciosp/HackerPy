# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:40:38 2017

@author: Lúcio
"""

# Take inputs
#s = list(input().strip())

# Testcases
#s = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'd']
s = ['b', 'a', 'a', 'b']
s = ['b', 'b']

#Algorithm
i = 0
while i < len(s) and len(s) != 0:
    if i != len(s)-1 and s[i] == s[i+1]:
        del(s[i:i+2])
        i = 0
    else:
        i += 1
    
if s == []: 
    print('Empty String')
else:
    print(str.join('', s))