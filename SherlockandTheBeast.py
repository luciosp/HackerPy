# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 20:30:25 2017

@author: Lúcio
"""

#!/bin/python3

import sys
from math import floor

#t = int(input().strip())
t = 4
for a0 in range(t):
    # Take inputs
    n = int(input().strip())
    #n = 5
    
    # Algorithm
    # Find possible combinations
    possibles = []
    for num_of_5 in range(1, floor(n/3) + 1):
        #print('num_of_5 = ' + str(num_of_5))
        if (floor(n/3) == 1) and (n%3 == 2):
            possibles.append([5, 0])
            break
        elif (n%(num_of_5*3))%5 == 0:
            num_of_3 = n%(num_of_5*3)
            #print('num_of_3 = ' + str(num_of_3))
            possibles.append([num_of_3, num_of_5*3])                
    #print('possibles = ' + str(possibles))
        
    # Construct number
    if possibles != []:
        for pair in possibles:
            num = pair[1]*'5' + pair[0]*'3'
            print(num)
    else:
        print('-1')
