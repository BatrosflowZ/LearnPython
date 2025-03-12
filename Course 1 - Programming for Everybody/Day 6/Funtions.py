# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 19:42:00 2025

@author: batro
"""

#Open IsPrime()
def IsPrime(value):
    print('Validanting Prime Numbers')
    seeker = value - 1
    residual = 0
    isPrime = True
    
    while seeker > 1:
        residual = value % seeker
        if residual == 0 :
            isPrime = False
        seeker = seeker - 1
        
    return isPrime
    
#Close IsPrime()

sMessage = 'Enter a number to validate for prime: '
try:
    seekForPrime = int(input(sMessage))
    print(IsPrime(seekForPrime))
except:
    print('Invalid input parameter')
    
    