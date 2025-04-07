# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 19:41:51 2025

@author: batro
"""

def multiplicationTable(multiple):
    
    product = 0

    
    for i in range(1, 11, 1):
        product = multiple * i
        print(product, end = " ")

   
# main program
strMesssage = 'Enter a number: '

try:
    intNumber = int(input(strMesssage))
    multiplicationTable(intNumber)

except:
    print('Errror - Enter a integer value')