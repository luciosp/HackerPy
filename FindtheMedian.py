# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:27:39 2017

@author: Lúcio
"""

from math import floor

def findMedian(lst):
    lst.sort()
    median = lst[floor(len(lst)/2)]
    return median

if __name__ == '__main__':
    # Take inputs
    #n = int(input().strip())
    #ar = list(map(int,input().split()))
    
    # Testcases
    ar = [0, 1, 2, 4, 6, 5, 3]

    print(findMedian(ar))