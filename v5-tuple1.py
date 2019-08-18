#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:07:05 2019

@author: vnit-stu
"""

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums +(t[0],)
        if t[1] not in words:
            words =words + (t[1],)
    min_n=min(nums)
    max_n=max(nums)
    print(min_n, max_n)
    unique_words =len(words)
    return (min_n, max_n,unique_words)

tswift =((2014,"Kat"),
         (2014,"Harry"),
         (2012,"Jack"),
         (2010, "abc"),
         (2008, "Joe"))
(min_n, max_n,unique_words)=get_data(tswift)

print("from",min_n,"to", max_n,unique_words)