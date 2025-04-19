# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:47:24 2025

@author: batro
"""

def printIncreasingPower(x):
    i=1
    iPower = 0
    iPower = pow(i,2)
    while iPower <=  x:
        print("i = ", i, " iPower = ", iPower)
        #print(iPower, end = " ")
        i = i + 1
        iPower = pow(i,2)

#main program
try:
    inputValue = int(input("x = "))
    printIncreasingPower(inputValue)
except:
    print("Error - Enter and interger")