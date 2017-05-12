'''
Method to receive string which contains a set of parenthesis

text within those parenthesis is to be reversed

return the string with parenthesis removed
'''

word = "ab(c(fed)gh)i"


def reverseParentheses(s):
    word = list(s)
    y = 0
    z = 0

    for i in range(len(word)):

        if word[i] == '(':

            y = i

        elif word[i] == ')':

            z = i

    rev = word[y + 1: z]
    word[y:z + 1] = rev[::-1]
    print word
    if '(' in word:
        return reverseParentheses(word)
    return word

    #return (''.join(word))



   #` print y


print(reverseParentheses(word))


