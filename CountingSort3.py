# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:06:19 2017

@author: Lúcio
"""

def countingSort(l):
    counter = [0]*100
    for i in l:
        counter[i[0]] += 1
        
    output = []
    s = 0
    for idx in range(len(counter)):
        i = counter[idx]
        s += i
        output.append(s)
    return output

if __name__ == '__main__':
    # Take inputs
    #n = int(input().strip())
    ar = [list(input().strip().split(' ')) for c in range(n)]
    ar = [[int(e[0]), e[1]] for e in ar]
    
    # Testcases
    #ar = [[4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'], [4, 'the']]
    out = [1, 3, 5, 6, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ,10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    print(' '.join(map(str, countingSort(ar))))
    if(countingSort(ar) == out):
        print("Correct")
    else:
        print("WRONG")