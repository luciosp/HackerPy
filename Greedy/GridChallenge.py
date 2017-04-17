# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:55:59 2017

@author: Lúcio
"""

t = int(input().strip())
for _ in range(t):

    # Take inputs
    n = int(input().strip())
    grid = [sorted(list(input())) for j in range(n)]
    
    # Algorithm
    tempColumn = []
    ans = 'YES'
    for col in range(n):
        for row in range(n):
            tempColumn.append(grid[row][col])
        
        if tempColumn == sorted(tempColumn):
            del(tempColumn[:])
        else:
            ans = 'NO'
            break
          
    print(ans)