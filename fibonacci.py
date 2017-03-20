def fibonacci(n):
    numToPrint = 0
    nextNum = 1
    print(numToPrint)
    for i in range(n):
        numToPrint += nextNum
        nextNum = numToPrint - nextNum
    print(numToPrint)

fibonacci(100)