
'''

The object of this task is to return true if a given word is a palidrome

IE

dad = dad   TRUE

jack = kcaj FALSE
'''

def checkPalindrome(inputString):
    x = inputString.lower()

    y = x[::-1]

    if x == y: return(True)
    else:
        return(False)
