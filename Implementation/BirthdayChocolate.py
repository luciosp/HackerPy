# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:35:10 2017

@author: Lúcio
"""

def getWays(squares, d, m):
    counter = 0
    i = 0
    while (i + m) <= len(squares):
        if sum(squares[i:i + m]) == d:
            counter +=1
        i += 1
    
    return counter
        

if __name__ == '__main__':
    # Take inputs
    #n = int(input().strip())
    #s = list(map(int, input().strip().split(' ')))
    #d, m = input().strip().split(' ')
    #d, m = [int(d),int(m)]
    
    # Testcases
    n = 5
    s = [1, 2, 1, 3, 2] 
    d, m = [3, 2]
    
    print(getWays(s, d, m))