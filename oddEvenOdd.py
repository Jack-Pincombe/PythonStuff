import random
'''
For a recent role in cyber crime I was given a number of tasks

one being that a pop so to speak would pop up stating

    ODD ODD EVEN

    then id check ok and it would display 3 numbers

    7 4 2

    I would then have to state how many of the numbers matched the statement.


'''







def getRan():
    nums = []
    for i in range(3):
        nums.append(random.randint(0,1))

    return nums

def usrIn():
    user = []

    for i in range(3):
        user.append(input("Odd(O) or Even(E):.... "))
    print(user)


def gen1(x,y):

    totalCorrect = 0

    div = []
    for i in x:
        if i == 0:
            div.append("even")
        else:
            div.append("odd")

    for i in range(3):
        if div.i

def getNum():

    num = []

    for i in range(3):
        num.append(random.randint(1,9))

    return(num)




def __main__():
    gen1(getRan())
    print(getNum())

__main__()



