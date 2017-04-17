# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 09:30:32 2017

@author: Lúcio
"""

#!/bin/python3

import sys
import re

time = input().strip()
#time = '07:05:45PM'
#time = '12:05:45AM'
#time = '12:00:00PM'

newHours = ''

splited = time.split(':')
hours = int(splited[0])
minutes = splited[1]

temp = re.split('(\d+)',splited[2])
seconds = temp[1]
period = temp[2]

if period == 'PM':
    if hours != 12:
        hours += 12
    newHours = str(hours)

if period == 'AM':
    if hours == 12:
        hours = 0
    newHours = '0' + str(hours)

newTime = str.join(':', (newHours, minutes, seconds))

print(newTime)