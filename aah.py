import sys

#method to return last 3 chars in a String
def slicing(name):

    x = len(name)
    x -= 3

    print(name[x::])



slicing("Jack")