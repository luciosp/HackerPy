# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:12:47 2017

@author: Lúcio
"""

MAX = 10000
def createCounter(lst):
    counter = [0]*MAX
    for e in lst:
        counter[e] +=1
    return counter


def beautifulPairs(counterA, lstB):
    # For an element in A, if there's a matching element in B, (Line 27 and 28)
    # this creates a "beautiful pair". (Line 29)
    # Each element can only be used once to create a beautiful pair. (Line 30)
    beautifulPairs = 0
    for element in lstB:
        if counterA[element] > 0:
            beautifulPairs += 1
            counterA[element] -= 1  
    
    # Additionaly, We MUST change exactly 1 element in B.
    # We attempt to change it to create 1 more beautiful pair. 
    # In the special case where we already have the max number of 
    # beautiful pairs, being forced to change it gives us 1 less 
    # beautiful pair.
    if beautifulPairs == len(lstB):
        beautifulPairs -= 1
    else:
        beautifulPairs += 1
    
    return beautifulPairs


if __name__ == '__main__':
    # There is no need to keep track of the values inside
    # the list. We just need to use a bucket (i.e., a counter
    # where the value is added by 1 in the respective index
    # when a number is present. For instance, counter = [0, 0, 0, 0]
    # list = [1, 2, 2, 3] => counter = [0, 1, 2, 1]).
    # Take inputs
    #n = int(input().strip())
    #a = createCounter(list(map(int, input().strip().split(' '))))
    #b = list(map(int, input().strip().split(' ')))

    # Testcases
    n = 3
    counterA = createCounter([1, 2, 2])
    lstB = [1, 2, 3]      
    print(beautifulPairs(counterA, lstB))