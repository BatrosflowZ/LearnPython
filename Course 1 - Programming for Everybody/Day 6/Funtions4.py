#3.11 Excercises


def computegrade(score):
    fScore = score
    if fScore >= 0.0 and fScore <= 1.0:
        if fScore >= 0.9:
            sMessage = 'A'
        elif fScore >= 0.8 and fScore < 0.9:
            sMessage = 'B'
        elif fScore >= 0.7 and fScore < 0.8:
            sMessage = 'C'
        elif fScore >= 0.6 and fScore < 0.7:
            sMessage = 'D'
        elif fScore < 0.6:
            sMessage = 'F'
    else:
        sMessage = 'Bad score'
    return sMessage

sMessage = 'Exercise 3: Scores'
print(sMessage)

try:
    sMessage = 'Enter a score: '
    fScore = float(input(sMessage))
    sMessage = computegrade(fScore)
      
except:
    sMessage = 'Bad score' 

print(sMessage)   
    
    
