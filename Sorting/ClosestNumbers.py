# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:57:55 2017

@author: Lúcio
"""

def findClosestNumbers(l):
    l.sort()
    closest = []
    maxDiff = l[-1] - l[0]
    for i in range(1, len(l)):
        curDiff = l[i] - l[i-1]
        #print('l[i-1] = ' + str(l[i-1]) + ', l[i] = ' + str(l[i]))
        #print(curDiff)
        if curDiff < maxDiff:
            maxDiff = curDiff
            del(closest[:])
            closest.append([l[i-1], l[i]])
        elif curDiff == maxDiff:
            closest.append([l[i-1], l[i]])
    return closest

if __name__ == '__main__':
    # Take inputs
    #n = int(input().strip())
    #ar = list(map(int,input().split()))
    
    # Testcases
    #ar = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854] 
    #ar = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]
    ar = [5, 4, 3, 2]
    
    print(' '.join(map(str, [' '.join(map(str, e)) for e in findClosestNumbers(ar)])))