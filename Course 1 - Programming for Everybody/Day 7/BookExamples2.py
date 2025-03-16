#Loops and Iterations

sMessage = ''
lNumbers = [9, 41, 12, 3, 74, 15, 8, 110, 1, 4, 3, 43, 21, 62]
count = 0
total = 0
valueToBeFound = 3
foundValue = False

largest = smallest = None

for value in lNumbers:
    count = count + 1
    total = total + value
    
    if largest is None:
        largest = value
    elif largest < value:
        largest = value
    
    if smallest is None:
        smallest = value
    elif smallest > value:
        smallest = value
    
    if value == valueToBeFound and foundValue != True:
        foundValue = True
    
print('Count = ', count)
print('Sum = ', total)
print('Avg = ', total/count)
print('Max (calculated) = ', largest)
print('Max (using function) = ', max(lNumbers))
print('Min (calculated) = ', smallest)
print('Min (using function) = ', min(lNumbers))
print('There is a ', valueToBeFound)