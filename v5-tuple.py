#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:51:54 2019

@author: vnit-stu
"""

te =()

t= (2, 'mit', 3)
print(t[0])
print((2,'mit',3)+(5,6))
print(t[1:2])
print(t[1:3])
print(len(t))
#t[1]=4 #error 

x=10
y=20
print(x,y)
(x,y)=(y,x)
print(x,y)

def quotient_and_remainder(x,y):
    q= x// y
    r=x % y
    return(q,r)

(quot, rem) = quotient_and_remainder(13,6)
print(quot , rem)