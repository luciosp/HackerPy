# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:09:33 2017

@author: Lúcio
"""

def returnMax(lst, MAX):
    counter = [0]*(MAX+1)
    for e in lst:
        counter[e] +=1
    return counter.index(max(counter))


if __name__ == '__main__':
    # Take inputs
    #n = int(input().strip())
    #types = list(map(int, input().strip().split(' ')))
    
    # Testcases
    n = 6
    types = [1, 4, 4, 4, 5, 3] 
    
    print(returnMax(types, max(types)))