'''
Returning the largest possible product of two adajacent numbers
'''

x = [1,2,3,4,5,6,7,8,9]

def adjacentLargestNumbers(inputArray):
    largest = -1000

    for i in range(len(inputArray)-1):
        x = inputArray[i] * inputArray[i + 1]

        if x > largest:
            largest = x

    return(largest)

print(adjacentLargestNumbers(x))