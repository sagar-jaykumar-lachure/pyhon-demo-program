#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:50:56 2019

@author: vnit-stu
"""
import cv2
import numpy as np
#import imutils

i_original=cv2.imread('/home/vnit-stu/Desktop/car/car1.jpg')
cv2.imshow('Original', i_original)

i_original1= i_original.copy()

i_bw =cv2,cvtcolor(i_original , cv2.COLOR_BGR2GRAY)
i_bw= cv2. medianBlur(i_bw,7)
cv2.imshow('gray scale image', i_bw)

th_gauss= cv2.adaptiveThreshold(i_bw, 255 ,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                cv2.THRESH_BINARY,11,2)
cv2.imshow(th_gauss)

