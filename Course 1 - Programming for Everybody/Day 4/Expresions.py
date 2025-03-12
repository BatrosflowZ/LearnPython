''' Day 4 - 2.1 Expressions'''
''' Chose Mnemonic varible Names'''
''' Camel ThisIsAVariable name'''

import random


print('This is Day 4 - Expressions')

PI = 3.1415

str =  '<class \'str\'>' 

sRadious = input('Enter the radious')
print(sRadious)

if sRadious != str:
    iRadious = int(sRadious)
else:
    iRadious = 0
    
area = PI*iRadious**2

x = 1 + 2 ** 3 / 4 * 5

y = random.random() % 10


print('PI = ', PI, ', iRadious = ',iRadious)
print('area = ', area)
print('x = ', x)
print('y = ', y)

print(float(99) + 100)
i = 42

sVal = '123'
print(type(sVal))
'''print(sVal + 1)'''
iVal = int(sVal)
type(iVal)
print(iVal)


