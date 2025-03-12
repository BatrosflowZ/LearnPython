#Day 4 - Expressions 2 

#Defining input variables...
sMessage = "Value"
sSeparator = '-' * 5
iEvenIndicator = 2


sMessage = ' Section 1 - Input values '
print(sSeparator + sMessage + sSeparator)

sMessage = 'Enter a number: '
inputVariable = input(sMessage)

inputVariable = int(float(inputVariable))

c = inputVariable % iEvenIndicator
if c != 0:
    sMessage = '[' + str(inputVariable) + '] is an odd number'
    print(sMessage)
else:    
    sMessage = '[' + str(inputVariable) + '] is an even number'
    print(sMessage)

sMessage = ' Section 1 - Input float values and round it '
print(sSeparator + sMessage + sSeparator)
sMessage = 'Enter a number with more than 3 decimals (Ex.: 3.145312): '
inputVariable = input(sMessage)
print(round(float(inputVariable),2))

sMessage = ' Section 2 - Building strings '
print(sSeparator + sMessage + sSeparator)

sValue = "PI = "
iValue = 3.14
sConcat = sValue + str(iValue)
print(sConcat)

sMessage = ' Section 3 - Building strings lists '
print(sSeparator + sMessage + sSeparator)

words = ['Pedro', 'Natalie', 'Peki', 'Fishies', '...']

for word in words:
    print (word)

sMessage = ' Section 4 - Exercise Celsius to Fahrenheit '
print(sSeparator + sMessage + sSeparator)
sMessage = 'Enter a value in Celsius: '
inpCelsius = input(sMessage)
fCelsius = float(inpCelsius)
fFahrenheit = round(fCelsius * (9/5) + 32, 2)
sMessage = '--> ' + str(fCelsius) + 'C = ' + str(fFahrenheit) + 'F'
print(sMessage)

