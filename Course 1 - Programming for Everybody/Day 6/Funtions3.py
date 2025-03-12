#Exercise

#3.11 Excercises

def computpay(hours, rate):
    fOTF = 1.5
    fOTT = 40.0
    fHr = hours
    fRate = rate
    if fHr <= fOTT:
        fTotalPay = fHr * fRate
    else:
        fDelta = fHr - fOTT
        fNormalPay = fOTT * fRate
        fOvertimePay = fDelta * fRate * fOTF
        fTotalPay = fNormalPay + fOvertimePay

    return fTotalPay

sMessage = 'Exercise 6: overtime'
print(sMessage)

try:
    sMessage = 'Enter the number of hours you worked = '
    fHr = float(input(sMessage))
    
    sMessage = 'Enter the rate per hour = '
    fRate = float(input(sMessage))
except:
    sMessage = 'Error, please enter a numeric input'
    print(sMessage)
    
sMessage = 'The total pay for the ' + str(fHr) + 'hrs is ' + str(computpay(fHr, fRate))
print(sMessage) 
    
