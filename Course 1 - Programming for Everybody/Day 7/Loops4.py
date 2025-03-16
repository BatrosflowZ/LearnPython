#Loops and Iterations

sMessage = ''
lNumbers = [9, 41, 12, 3, 74, 15, 8, 110, 1, 4, 3, 43, 21, 62]
count = 0
sum = 0
valueToBeFound = 3
foundValue = False

max = min = None

for value in lNumbers:
    count = count + 1
    sum = sum + value
    
    if max is None:
        max = value
    elif max < value:
        max = value
    
    if min is None:
        min = value
    elif min > value:
        min = value
    
    if value == valueToBeFound and foundValue != True:
        foundValue = True
    
print('Count = ', count)
print('Sum = ', sum)
print('Avg = ', sum/count)
print('Max = ', max)
print('Min = ', min)
print('There is a ', valueToBeFound)
