'''
Method to receive string which contains a set of parenthesis

text within those parenthesis is to be reversed

return the string with parenthesis removed
'''

word = "ab(c(fed)gh)i"


def reverseParentheses(s):
    x = list(s)

    count = 0
    cleft = 0

    for i in x:
        if i == '(' or i == ')':
            count+=1

    left = count // 2

    for i in x:
        if i == '(':
            cleft += 1


    print(count)
    print(left)



   #` print y


print(reverseParentheses(word))


