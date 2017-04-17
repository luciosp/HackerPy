# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 12:35:38 2017

@author: Lúcio
"""

def insertionSort(lst):
    count = 0
    for i in range(1, len(lst)):
        j = i-1
        key = lst[i]
        while (j >= 0) and (lst[j] > key):
           lst[j+1] = lst[j]
           count += 1
           j -= 1
        lst[j+1] = key
    return count

if __name__ == '__main__':
    # Take inputs
    t = int(input().strip())
    while t > 0:
        n = int(input().strip())
        ar = list(map(int,input().split()))
    
        # Testcases
        #ar = [0, 1, 2, 4, 6, 5, 3]

        print(insertionSort(ar))
        t -= 1