# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:30:25 2017

@author: Lúcio
"""

t = int(input().strip())
#t = 1
for a0 in range(t):
    # Take inputs
    n = int(input().strip())
    #n = 11
    
    # Algorithm
    c = 5 * (2 * n % 3);
    if c > n:
        print('-1')
    else:
        print((n - c)*'5' + c*'3')

