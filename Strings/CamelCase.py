# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 18:52:25 2017

@author: Lúcio
"""

# Take inputs
#s = input().strip()

#Testcases
s = 'saveChangesInTheEditor'

#Algorithm
total = sum(1 for c in s if c.isupper()) + 1
print(total)