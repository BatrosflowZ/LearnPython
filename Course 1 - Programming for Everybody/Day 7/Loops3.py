#Loops and Iterations

max = 0
sMessage = ''
lNumbers = [9, 41, 12, 3, 74, 15, 8, 110, 1, 4, 3, ]
count = 0
sum = 0

print('Start counting count = ', count, 'sum = ', sum )
for value in lNumbers:
    count = count + 1
    sum = sum + value
    if max < value:
        max = value
    print('Count =', count, ' Sum = ', sum)

print('Count = ', count)
print('Sum = ', sum)
print('Avg = ', sum/count)
print('Max num = ', max)
