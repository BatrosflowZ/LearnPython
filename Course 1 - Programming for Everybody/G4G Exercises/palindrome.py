# Test for plindrome

# Fuction recieves a string and validates if it is a palindrome
def isPalindrome(word):
    palindrome = False    
    wordLenght = len(word)
    index = 0
             
    while index < wordLenght/2:        
        if word[index] == word[(wordLenght - 1) - index]:
            palindrome = True
        else:
            palindrome = False
            break
        index += 1
    return palindrome

# Main program

strInitMessage = '*** Program Start ***'
strEndMessage = '*** Program End ***'
strMessage = 'Enter a word to test for palindrome: '
strErrorMessage = 'Error: '

testPalindrome = False
strWord = ''

print(strInitMessage)

try:
    strWord = str(input(strMessage))
    testPalindrome = isPalindrome(strWord)
    print('The word', strWord, 'tested', testPalindrome, 'for palindrome.')
except:
    print(strErrorMessage, 'input not valid.')

print(strEndMessage)