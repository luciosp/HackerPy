# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 08:59:22 2017

@author: Lúcio
"""

#!/bin/python3

import sys


# Take inputs
#s,t = input().strip().split(' ')
#s,t = [int(s),int(t)]
#a,b = input().strip().split(' ')
#a,b = [int(a),int(b)]
#m,n = input().strip().split(' ')
#m,n = [int(m),int(n)]
#apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
#orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

# Testcase
s,t = [7, 11]
a,b = [5, 15]
m,n = [3, 2]
apple = [-2, 2, 1]
orange = [5, -6]

# Algorithm
print([1 for ap in apple if(a + ap) >= s and (a + ap) <= t].count(1))
print([1 for og in orange if(b + og) >= s and (b + og) <= t].count(1))

