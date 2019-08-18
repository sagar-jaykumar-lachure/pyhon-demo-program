#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:07:32 2019

@author: vnit-stu
"""
cube= 8120601
for guess in range(abs(cube+1)):
    if guess**3>= abs(cube):
        break
if guess**3!= abs(cube):
     print(cube, 'is a perfect cube')
else:
    if cube < 0:
        guess = -guess
        print('cube root of '+ str(cube)+ ' is '+str(guess) )
