# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:23:08 2017

@author: Lúcio
"""

def insertionSort(l):
    shifts  = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           shifts  += 1
           j -= 1
        l[j+1] = key
    return l, shifts 


qSwap = 0
def swap(l, i, j):
    global qSwap
    l[i], l[j] = l[j], l[i]      
    qSwap += 1
    

def partition(l, lo, hi):
    i = lo - 1
    pivot = l[hi]
    for j in range(lo, hi):
        if l[j] <= pivot:
            i += 1
            swap(l, i, j)
            #l[i], l[j] = l[j], l[i]
    swap(l, i+1, hi)        
    #l[i+1], l[hi] = l[hi], l[i+1]
    #print(' '.join(map(str, l)))
    
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
    ar1 = ar[:]
    ar2 = ar[:]
    
    # Testcases
    #ar1 = [1, 3, 9, 8, 2, 7, 5]
    #ar2 = [1, 3, 9, 8, 2, 7, 5]

    _, iSwap = insertionSort(ar1)
    inPlaceQuickSort(ar2, 0, len(ar2)-1)
    print(str(iSwap - qSwap))