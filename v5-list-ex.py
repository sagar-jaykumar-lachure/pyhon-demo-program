#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:54:39 2019

@author: vnit-stu
"""
a=1
b=a
print(a)
print(b)

warm= ['red', 'yellow', 'orange']
hot =warm
print(warm)
hot.append('pink')
print(hot)
print(warm)

cool=['blue', 'green', 'gray']
chill= cool[:]
chill.append('black')
print(chill)
print(cool)


warm= ['red', 'yellow', 'orange']
sortedwarm=warm.sort()
print(warm)
print(sortedwarm)

cool=['blue', 'green', 'gray']
sortedcool= sorted(cool)
print(cool)
print(sortedcool)

warm= [ 'yellow', 'orange']
hot =['red']
brightcolors=[warm]
brightcolors.append(hot)
print(brightcolors)
hot.append('pink')
print(hot)
print(brightcolors)