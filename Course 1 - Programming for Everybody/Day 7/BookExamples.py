#Book Examples - Loops


#variables
example = 5
n = 100
count = 0
sMessage = 'Count = '
sText = ''
#variables

#print while the value of count is smaller than n
if example == 1:
    while count < n:
        count += 1 #short cut for count = count +1    
        print(sMessage, count)


# usage of break and continue
if example == 2:
    sMessage = 'Enter a line of text. Lines starting with # will be ignore.'
    print(sMessage)
    sMessage = '-> '    
    
    while True:
        line = input(sMessage)        
        if line[0] == '#':
            continue
        if line == 'done':
            break
        sText += line + '\n'
    print(sText)
    
    
#iterates through the list of friends.    
if example == 3:
    sMessage = 'Friend = '
    friends = ['Peki', 'Nati', 'Pedro', 'Trevor', 'Igna']
    for friend in friends:
        print(sMessage, friend)
    print('Done!')
 
    
#count items in tha list    
if example == 4:
    count = 0
    sMessage = ''
    numbers = [9, 41, 12, 3, 74, 15, 8, 110, 1, 4, 3, 43, 21, 62]
    for number in numbers:
        count += 1
    sMessage = 'Using a counter, the list has ' + str(count) + ' numbers.'
    print(sMessage)
    sMessage = 'Using the len() function, the list has ' + str(len(numbers)) + ' numbers.'
    print(sMessage)
    
#sums the values in a list
if example == 5:    
    sMessage = ''
    total = 0
    numbers = [9, 41, 12, 3, 74, 15, 8, 110, 1, 4, 3, 43, 21, 62]
    for number in numbers:
        total += number
    sMessage = 'Adding one by one, the total is ' + str(total) + '.'
    print(sMessage)
    sMessage = 'Using the sum() function, the total is ' + str(sum(numbers)) + '.'
    print(sMessage)
