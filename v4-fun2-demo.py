#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:08:41 2019

@author: vnit-stu
"""

def f(y):
    x =1
    x += 1
    print(x)

x=5
f(x)
print(x)



def g(y):
    print(x)
    print(x+1)

x=5
g(x)
print(x)


# =============================================================================
# def h(y):
#     x +=1
#     
# x=5
# h(x)
# print(x)
# 
# =============================================================================

def g(x):
    def h():
        x='abc'
    x=x+1
    print('g:x=', x)
    h()
    return x

x=3
z=g(x)