# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 13:51:18 2025

@author: sanja
"""

print("Welcome to Python Pizza Calculator")
size_of_pizza = str.upper(input("Enter Size of Pizza S,M,L:"))
include_pepperoni=str.upper(input("Include pepperoni in Pizza (Y/N):"))
exta_cheese=str.upper(input("Extra cheese in Pizza (Y/N):"))
price_of_pizza=0
if (size_of_pizza == "S"):
    price_of_pizza = 15
    if (include_pepperoni == "Y" ):
        price_of_pizza += 2   
elif(size_of_pizza == "M"):
    price_of_pizza = 20
    if (include_pepperoni == "Y" ):
        price_of_pizza += 3  
elif(size_of_pizza == "L"):
    price_of_pizza = 25
    if (include_pepperoni == "Y" ):
        price_of_pizza += 3  
else:
    print("Invalid Pizza Size")
if (exta_cheese)== "Y" ):
    price_of_pizza += 1
print(f"Price of Pizza is {price_of_pizza}$")


    