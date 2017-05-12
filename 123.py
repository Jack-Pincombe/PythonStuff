import sys

print(sys.version)

def adjacentElementsProduct(inputArray):
    largest = 0
    t = 0
    y = 0

    for i in range(len(inputArray)):
        for j in range(len(inputArray) - 1):
            x = inputArray[i] * inputArray[j + 1]
            if x > largest:
                largest = x
                t = inputArray[i]
                y = inputArray[j]

        return(t,y)

def isParadim(word):

    x = str(word.lower()) # converts the inputed word into lower case.
    y = x[::-1] # reversing the word
    if x == y:
        return "is a paradim"
    else:
        return word +" is not a paradim"


def fibonacci(x):
    total = 0

    for i in range(1,x):
        print(i)



inputArray = [12,32,53,34,54,23,456,4]
name = "Jack"


def question1():
    values = []
    for i in range(2000,3200):
        if i % 7 == 0 and i % 5 != 0:
            values.append(i)
    print(values)

question1()

def question2(x):
    total = 1
    for i in range(1,x + 1):
        total = total * i
    print total
question2(5)

def question3(num):
    if num % 1 != 0:
        num += num - (num % 1) #rounding a float to an int (always rounds down
        num = int(num)
    for i in range(1, num + 1):
        print(str(i) +": " + str((i * i)))
question3(7.3)
r
def question4():
    y = []
    x = ""
    t = "stop"
    while True:
        x = raw_input("Please enter a number: \n ...")
        print(x)
        if str(x) == t:
            return y
            return False
        else:
            y.append(x)
    return y


class Tester:
    def __init__(self):
        self.s = ""

    def addName(self):
        self.s = raw_input("Please enter your name:")


    def getname(self):
        print self.s.upper()

#method to return last 3 chars in a String
def slicing(name):

    return name

print(slicing(jack))


