# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 09:11:17 2017

@author: Lúcio
"""

#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

#n = 4
#height = [3, 2, 1, 3]

maxHeight = max(height)
numBlowCandles = height.count(maxHeight)


print(str(numBlowCandles))
