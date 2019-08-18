#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:37:08 2019

@author: vnit-stu
"""
#####################################
# EXAMPLE: comparing fibonacci using memoization
#####################################
def fib(n):
    if n==1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1)+fib(n-2)

print(fib(34))

def fib_efficient(n ,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans

d={1:1, 2:2}

print(fib_efficient(34, d))
    
