#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:09:01 2019

@author: vnit-stu
"""
# =============================================================================
# s="abc"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[-1])
# print(s[-2])
# print(s[-3])
# =============================================================================

s="abcdefghi"
# =============================================================================
# print(s[3:6])
# print(s[3:6:2])
# print(s[::])
# print(s[::-1])
# print(s[4:1:-2])
# =============================================================================

for index in range(len(s)):
    if s[index] =='i' or s[index] =='u':
        print("there is an i or u")


for char in s:
    if char =='i' or char =='u':
        print("there is an i or u")
