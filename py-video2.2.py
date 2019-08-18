#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 13:33:47 2019

@author: vnit-stu
"""
x = float(input("enter a float no"))
y = float(input("enter a float no"))

if x==y:
    print("x and y are equal")
    if y!=0:
        print("Therefor, x/y is", x/y)
elif x<y:
    print("x is smaller ")
else:
    print("y is smaller")
print("thanks!")

