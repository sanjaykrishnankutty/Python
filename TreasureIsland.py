# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 14:12:46 2025

@author: sanja
"""
def Game_over():
    print ("Game Over!")
    
print("Welcome to the treasure island!")
print("Your mission is to find the treasure..")
left_or_right= str.upper(input("Do you want to go left or right:"))
if (left_or_right == "RIGHT"):
    Game_over()
else:
    swim_or_wait=str.upper(input("Do you want to swim or wait?:"))
    if (swim_or_wait == "SWIM"):
        Game_over()
    else:
        select_door=str.upper(input("Select door color (Red,Blue,Yellow)"))
        if(select_door == "YELLOW"):
            print("You Win!")
        else:
            Game_over()
        

    
