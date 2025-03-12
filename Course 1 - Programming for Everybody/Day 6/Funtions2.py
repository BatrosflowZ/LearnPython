#Funtions from the book

import math
import random
#import time

print(math)

def cosInD(degrees):
    
    radians = math.radians(degress)
    return math.cos(radians)


lStr = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


for d in range(1000):
    degress = random.randint(0, 360)
    degress = degress
    cos_x = round(cosInD(degress),2)
    print('Cos(' + str(degress) + ') = ', cos_x)
    #time.sleep(0.001)

print('->', random.choice(lStr))
    