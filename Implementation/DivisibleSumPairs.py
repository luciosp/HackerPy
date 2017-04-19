# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:52:36 2017

@author: Lúcio
"""

MAX = 7
def createCounter(lst):
    counter = [0]*MAX
    for e in lst:
        counter[e] +=1
    return counter


def getDivisibleSumPairs(s, k):
    counterS = createCounter(s)
    numValidParis = 0
    for i in range(1, len(counterS)):
        for j in range(i + 1, len(counterS)):
            if (i + j)%k == 0:
                numValidParis += counterS[i] * counterS[j]
    
    return numValidParis
    

if __name__ == '__main__':
    # Take inputs
    #n,k = input().strip().split(' ')
    #n,k = [int(n),int(k)]
    #a = list(map(int, input().strip().split(' ')))
    
    # Testcases
    n, k = [6, 3]
    s = [1, 3, 2, 6, 1, 2] 
    
    print(getDivisibleSumPairs(s, k))