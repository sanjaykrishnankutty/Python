# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 13:32:29 2025

@author: sanja
"""

print("Enter your height in cms: ")
height_in_cms= int(input())
print("Enter you age: ")
age=int(input())
if (height_in_cms > 120):
    if (age <12):
        print("Please pay $5 for your ticket")
    elif(age>=12 and age <=18):
        print("Please pay $7 for your ticket")
    else:
        print("Please pay $12 for your ticket")
else:
    print("Sorry you cant ride the roller coaster!")