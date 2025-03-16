#Loops and Iterations

max = 0
sMessage = 'Enter password to exit loop ->'
lNumbers = [9, 41, 12, 3, 74, 15, 8, 110, 1]


for n in lNumbers:
    print('max = ', max, ' and n = ', n)
    if max < n:
        print('n = ', n, ' is larger than previuos max = ', max)
        max = n       
print('Max num = ', max)
    



