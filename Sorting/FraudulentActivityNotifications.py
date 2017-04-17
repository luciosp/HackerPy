# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:21:11 2017

@author: Lúcio
"""

from math import floor
import bisect

def calculateMedian(lst):
    remainder = len(lst)%2
    half = len(lst)/2
    if remainder != 0:
        return lst[floor(half)]
    else:
        higherIdx = int(len(lst)/2)
        lowerIdx = int(higherIdx - 1) 
        return (lst[lowerIdx] + lst[higherIdx])/2



def notifyClient(expenditures, windowOfDays):
    windowArray = []
    numNotifications = 0
    
    # Fill the initial array up to window's size
    for idx in range(d):
        bisect.insort(windowArray,expenditures[idx])
        #print(windowArray)
        #print(expenditures[idx])
        
    # Find fraudulent notifications
    for idx in range(d, len(expenditures)):
        
        # Calculate median
        if d%2 == 0:
            lower = windowArray[int(len(windowArray)/2)]
            higher = windowArray[int(len(windowArray)/2 - 1)]
            median = (lower + higher)/2
        else:
            median = windowArray[int(len(windowArray)/2)]
        
        if expenditures[idx] >= 2*median:
            numNotifications += 1
        
        # Find the index in the windowArray that correspond to the element
        # with lowest index in the expenditures array.
        toRemove = bisect.bisect(windowArray, expenditures[idx - d]) - 1
        
        # Remove the element from the window
        windowArray.pop(toRemove)
        # Add the next element from expenditures to the windowArray
        bisect.insort(windowArray, expenditures[idx])
        
    return numNotifications  


def notifyClient_old(expenditures, windowOfDays):
    numNotifications = 0
    i = 0
    j = windowOfDays
    while j <= len(expenditures) - 1:
        median = calculateMedian(expenditures[i:j])
        if expenditures[j] >= 2*median:
            numNotifications += 1
        i += 1
        j += 1
    return numNotifications 


if __name__ == '__main__':
    # Take inputs
    #n,d = input().strip().split(' ')
    #n,d = [int(n), int(d)]
    #ar = list(map(int,input().split()))
    
    # Testcases
    d = 5
    ar = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    
    print(notifyClient(ar, d))