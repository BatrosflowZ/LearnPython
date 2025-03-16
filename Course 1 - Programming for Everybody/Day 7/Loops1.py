#Loops and Iterations

loopCounter = 0
sMessage = 'Enter password to exit loop ->'

'''
#Loop starts
while True:    
    line = input(sMessage)
    if line == 'peki':
        break    
    print('Wrong password!')
#loop ends
print('Well done')
'''

'''
print('Loop counting started')
sMessage = 'Counting: '
while loopCounter < 10:
    print(sMessage, loopCounter)
    # inp = input('--> ')
    loopCounter = loopCounter + 1
print('Loop finished')
'''

friends = ['Jon', 'Nat', 'Pedro', 'Juan']
for friend in friends:
    print(friend)
print('Blastoff')



