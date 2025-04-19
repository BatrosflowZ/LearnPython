# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:37:01 2025

@author: batro
"""

def printInDecreasing(x):
    
    while x > 0:
        print(x, end = " ")
        x = x - 1
    print(x, end = " ")

#main program

try:
    inputValue = int(input("X = "))
    printInDecreasing(inputValue)
except:
    print("Error - Enter and interger")
        