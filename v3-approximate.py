#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:24:27 2019

@author: vnit-stu
"""
cube=10000
epsilon = 0.1
guess =0.0
increment = 0.0001
num_guesses = 0
while abs(guess**3-cube) >=epsilon and guess <= cube:
    guess += increment
    num_guesses +=1
print('num_guesses =', num_guesses)
if abs(guess**3 -cube) >=epsilon:
    print('failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of ', cube)
