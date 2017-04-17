# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:50:50 2017

@author: Lúcio
"""

def countingSort(inputList):
    k = 100
    count = [0]*k
    for x in inputList:
        count[x[0]] += 1
    
    total = 0
    for i in range(k):
        oldCount = count[i]
        count[i] = total
        total += oldCount
    
    # Original Counting Sort
    #output = [0]*len(inputList)
    #for x in inputList:
    #    output[count[x[0]]] = x
    #    count[x[0]] += 1
    
    # Required by client
    output = [0]*len(inputList)
    for i in range(len(inputList)):
        x = inputList[i]
        if i >= round(len(inputList)/2):
            output[count[x[0]]] = x[1]
        else:
            output[count[x[0]]] = '-'
        count[x[0]] += 1
    
    return output
    
if __name__ == '__main__':
    # Take inputs
    #n = int(input().strip())
    #ar = [list(input().strip().split(' ')) for c in range(n)]
    #ar = [[int(e[0]), e[1]] for e in ar]
    
    # Testcases
    ar = [[0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [0, 'ij'], [4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']]
    #out = [[0, 'ab'], [0, 'ef'], [0, 'ab'], [0, 'ef'], [0, 'ij'], [0, 'to'], [1, 'be'], [1, 'or'], [2, 'not'], [2, 'to'], [3, 'be'], [4, 'ij'], [4, 'that'], [4, 'is'], [4, 'the'], [5, 'question'], [6, 'cd'], [6, 'gh'], [6, 'cd'], [6, 'gh']]
    out = '- - - - - to be or not to be - that is the question - - - -'

    print(' '.join(map(str, countingSort(ar))))
    if(countingSort(ar) == out):
        print("Correct")
    else:
        print("WRONG")