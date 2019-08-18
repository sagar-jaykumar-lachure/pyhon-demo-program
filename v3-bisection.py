#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 15:41:30 2019

@author: vnit-stu
"""
cube=10000
epsilon = 0.01
num_guesses = 0
low =0
high = cube
guess =(high+low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess= (high + low)/2.0
    num_guesses +=1
print('nume_guess =' ,num_guesses)
print(guess, 'is close to the cube root of ',cube)




### for number between 0 to .99
cube=0.99
epsilon = 0.0001
num_guesses = 0
low =0
high = cube+1
guess =(high+low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess= (high + low)/2.0
    num_guesses +=1
print('nume_guess =' ,num_guesses)
print(guess, 'is close to the cube root of ',cube)


##### for number being neagtive
cube=-27
epsilon = 0.01
num_guesses = 0
low =cube
high = 0
guess =(high+low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 > cube :
        high = guess
    else:
        low = guess
    guess= (high + low)/2.0
    num_guesses +=1
print('nume_guess =' ,num_guesses)
print(guess, 'is close to the cube root of ',cube)