#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:22:01 2019

@author: vnit-stu
"""
def is_even_ret(i):
    """
    Input: i is positive int returns true if i is even, 
    otherwise False
    """
    
    print("inside is_even")
    return i%2 ==0
print(is_even_ret(456714))

def is_even(i):
    """
    Input: i is positive int returns true if i is even, 
    otherwise False
    """
    
    print("inside is_even")
    i%2 ==0
print(is_even(456714))

for i in range(20):
    if is_even_ret(i):
        print(i)
    
        

def f(x):
    x=x+1
    print('in f(x): x=' ,x)
    return x

x=3
z=f(x)