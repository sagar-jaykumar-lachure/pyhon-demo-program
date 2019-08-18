#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 14:10:47 2019

@author: vnit-stu
"""
# =============================================================================
# def factorial_iter(n):
#     prod=1
#     for i in range(1,n+1):
#         prod *= i
#     return prod
# 
# print(factorial_iter(100))
# 
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# 
# print(factorial(100))
# =============================================================================

#p=factorial(365)/(factorial(335) * 365**5)
#print(p)

def mul_iter(a,b):
    res=0
    while b>0 :
        res +=a
        b -=1
    return res

print(mul_iter(45698789,4))

def mul(a,b):
    if b==1:
        return a
    else:
        return a+mul(a,b-1)
    
print(mul(456987,236))
    
def fib(x):
    """assumes x an int>=0
    return Fibonacci of x"""
    if x ==0 or x== 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(10))
        