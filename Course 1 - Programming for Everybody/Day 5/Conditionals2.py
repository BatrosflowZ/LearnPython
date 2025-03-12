#3.11 Excercises


sMessage = 'Exercise 1 and 2: overtime'
print(sMessage)

fOTF = 1.5
fOTT = 40.0

try:
    sMessage = 'Enter the number of hours you worked = '
    fHr = float(input(sMessage))
    
    sMessage = 'Enter the rate per hour = '
    fRate = float(input(sMessage))
except:
    sMessage = 'Error, please enter a numeric input'
    print(sMessage)
    
if fHr <= fOTT:
    fTotalPay = fHr * fRate
else:
    fDelta = fHr - fOTT
    fNormalPay = fOTT * fRate
    fOvertimePay = fDelta * fRate * fOTF
    fTotalPay = fNormalPay + fOvertimePay

sMessage = 'The total pay for the ' + str(fHr) + 'hrs is ' + str(fTotalPay)
print(sMessage) 
    
