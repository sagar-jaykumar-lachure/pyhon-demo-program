#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:22:43 2019

@author: vnit-stu
"""

a_list=[]
l=[2, 'a' ,4, [1,2]]
print(len(l))
print(l[0])
print(l[2]+1)
print(l[3])
#print(l[4])
i =2
print(l[i-1])

L=[1,2,3]
L[1]=5
print(L)

#iteration through list

total=0
for i in range(len(L)):
    total +=L[i]
print(total)

total=0
for i in L:
    total += i
print(total)

L.append(10)
print(L)

L1=[1,2,3]
L2=[4,5,6]
L3=L1+L2
print(L3)
L1.extend([0,6,3])
print(L1)
L1.remove(2)
L1.remove(3)
del(L1[1])
L1.pop()
print(L1)

s="I<3 cs"
list(s)
print(s.split('<'))
L =['a','b','c']
print(''.join(L))
print('_'.join(L))


L=[9,6,0,3]
sorted(L)
print(L)
L.sort()
print(L)
L.reverse()
print(L)