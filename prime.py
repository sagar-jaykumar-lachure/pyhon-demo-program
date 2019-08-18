#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:01:08 2019

@author: vnit-stu
"""
# =============================================================================
# num=24;i=2
# while i<n:
#     if num%i==0:
#         break
#     i+=1
# if num==i:
#         print("prime")
# else:
#         print("not prime")
# =============================================================================


n=347
j=0
for i in range(2,n//2):
    if n % i== 0:
        j=1
        break
if j==1:
    print('not prime')
else:
    print('  prime')