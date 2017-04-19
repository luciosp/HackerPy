# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:26:26 2017

@author: Lúcio
"""

def getDivisibleSumPairs(s, k):
    numValidParis = 0
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if (i != j) and (s[i] + s[j])%k == 0:
                numValidParis += 1
    
    return numValidParis

def nonDivisableSets(lst, k):
    return 0

if __name__ == '__main__':
    # Take inputs
    #n,k = input().strip().split(' ')
    #n,k = [int(n),int(k)]
    #s = list(map(int, input().strip().split(' ')))
    
    # Testcases
    n, k = [4, 3]
    s = [1, 7, 2, 4] 
    
    print(nonDivisableSets(s, k))