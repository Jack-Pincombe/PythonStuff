

def fibonacci(n):
    numToPrint = 0
    nextNum = 1
    for i in range(n):


        numToPrint += nextNum
        nextNum = numToPrint - nextNum


        print(numToPrint)

fibonacci(1000)