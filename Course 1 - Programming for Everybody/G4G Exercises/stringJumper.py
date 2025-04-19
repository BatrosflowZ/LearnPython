# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:23:36 2025

@author: batro
"""

def stringJumper(strWord):
    
    for i in range(0, len(strWord), 2):
        print(strWord[i], end = "")
        

#main program
word = str(input('Enter word: '))
stringJumper(word)
