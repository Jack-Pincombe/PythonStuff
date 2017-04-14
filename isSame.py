

#this is to determin how many common letter pairs there are in two words

'''
For example in cat and hat there are two pairs a and t

in abbccdd and abcd there are only 4 pairs
'''

s1 = "aaabbbbccccdddd"
s2 = "abcd"
print(s2)

for i in range(len(s1)):
    if s1[i] in s2:
        print s1[i]
        del s1[i]



print(s2)