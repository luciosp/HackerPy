# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:52:36 2017

@author: Lúcio
"""

def getDivisibleSumPairs(s, k):
    numValidParis = 0
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if (i != j) and (s[i] + s[j])%k == 0:
                numValidParis += 1
    
    return numValidParis
    

if __name__ == '__main__':
    # Take inputs
    #n,k = input().strip().split(' ')
    #n,k = [int(n),int(k)]
    #s = list(map(int, input().strip().split(' ')))
    
    # Testcases
    n, k = [6, 3]
    s = [1, 3, 2, 6, 1, 2] 
    
    print(getDivisibleSumPairs(s, k))