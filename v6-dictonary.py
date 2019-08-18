#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:04:37 2019

@author: vnit-stu
"""
grades = {'Ana':'B', 'John':'A+', 'Denise':'A', 'Katy':'A'}

print(grades['John'])
 
print(grades['Ana'])

grades['Sagar'] = 'A+'

print(grades)

print('Sagar' in grades)
print('abc' in grades)

grades['abc'] = 'B'

print(grades)

del(grades['abc'])

print(grades)

print(grades.keys())

print(grades.values())

d = {4:{1:0}, (1,3):"twelve", 'const':[3.14,2.7,8.44]}

print(d)