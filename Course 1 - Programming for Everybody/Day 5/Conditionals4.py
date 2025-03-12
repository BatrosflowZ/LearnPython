#3.11 Excercises


lfScores = [0.9, 0.8, 0.7, 0.6]
lsScores = ['A', 'B', 'C', 'D', 'F']

sMessage = 'Exercise 3: Scores'
print(sMessage)


try:
    sMessage = 'Enter a score: '
    fScore = float(input(sMessage))
    
    if fScore >= 0.0 and fScore <= 1.0:
        if fScore >= lfScores[0]:
            sMessage = lsScores[0]
            
        elif fScore >= lfScores[1] and fScore < lfScores[0]:
            sMessage = lsScores[1]
        elif fScore >= lfScores[2] and fScore < lfScores[1]:
            sMessage = lsScores[2]
        elif fScore >= lfScores[3] and fScore < lfScores[2]:
            sMessage = lsScores[3]
        elif fScore < lfScores[3]:
            sMessage = lsScores[4]  
    else:
        sMessage = 'Bad score'
    
except:
    sMessage = 'Bad score'

print(sMessage)   
    
    
