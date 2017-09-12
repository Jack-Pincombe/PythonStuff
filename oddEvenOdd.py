import random
import sys



'''
For a recent role in cyber crime I was given a number of tasks

one being that a pop so to speak would pop up stating

    ODD ODD EVEN

    then id check ok and it would display 3 numbers

    7 4 2

    I would then have to state how many of the numbers matched the statement.


'''
#create a list containing the three rand nums
def createNum():
    nums = []
    for i in range(3):
        nums.append(random.randint(0,1))

    return nums




#create a list of words
def createWord():

    word = []

    for i in range(3):

        x = random.randint(0,1)

        if x == 0:
            word.append("Odd")
        else:
            word.append("Even")
    return word

def play(nums, words):

    print(createNum())
    input("Press enter to continue")
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line
    print(createWord())










def __main__():
    play(createNum(),createWord())



__main__()





