# Odd or Even

#returs True if even, else False
def checkOddEven(var1):
    remainder = var1 % 2
    
    if remainder == 0:
        even = True
    else:
        even = False        
    return even


#program

message = 'Enter a value: '
evenTest = True

while (evenTest == True):
    try:
        x = int(input(message))
        evenTest = checkOddEven(x)
        print(evenTest)
    except:
        print('Enter only numbers')

    