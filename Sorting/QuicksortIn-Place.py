# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:18:08 2017

@author: Lúcio
"""

def partition(l, lo, hi):
    i = lo - 1
    pivot = l[hi]
    for j in range(lo, hi):
        if l[j] <= pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
    l[i+1], l[hi] = l[hi], l[i+1]
    print(' '.join(map(str, l)))
    return i+1
    
            

def inPlaceQuickSort(l, lo, hi):
    if (lo < hi):
        p = partition(l, lo, hi)
        inPlaceQuickSort(l, lo, p-1)
        inPlaceQuickSort(l, p+1, hi)

if __name__ == '__main__':
    # Take inputs
    n = int(input().strip())
    ar = list(map(int,input().split()))
    
    # Testcases
    #ar = [1, 3, 9, 8, 2, 7, 5]

    inPlaceQuickSort(ar, 0, len(ar)-1)