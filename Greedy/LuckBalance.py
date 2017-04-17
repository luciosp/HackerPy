# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 15:48:26 2017

@author: Lúcio
"""

# Initialize variables
importantBalance = []
notImportantBalance = []


# Take inputs
args = input().strip().split(' ')
n = int(args[0])
k = int(args[1])
for i in range(n):
    [l, t] = input().strip().split(' ')
    if t == '1':
        importantBalance.append(int(l))
    elif t == '0':
        notImportantBalance.append(int(l))
    else:
        print('Wrong entry.')        



# Testcases
"""
n = 6
k = 3
importantBalance = [5, 2, 1, 8]
notImportantBalance = [10, 5]
"""

# Algorithm
importantBalance.sort(reverse=True)
notImportantBalance.sort(reverse=True)

add = 0
subtract = 0
for elemt in importantBalance[0:k]:
    add += elemt

for elemt in notImportantBalance:
    add += elemt

for elemt in importantBalance[k:len(importantBalance)]:
    subtract += elemt


#print(add)
#print(subtract)
print(add - subtract)

