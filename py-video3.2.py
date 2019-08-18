#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:51:58 2019

@author: vnit-stu
"""
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cherr for you! Enter a word:")
times = int(input("Enthusiasm level (1-10)"))

i=0
while i<len(word):
    char =word[i]
    if char in an_letters:
        print("give me an "+char +"! "+ char)
    else:
        print("give me a "+char +"! "+ char)
    i +=1
print("what does that spell?")
for i in range(times):
    print(word ,"!!!")


    
for char in word:
    if char in an_letters:
        print("give me an "+char +"! "+ char)
    else:
        print("give me a "+char +"! "+ char)
print("what does that spell?")
for i in range(times):
    print(word ,"!!!")

