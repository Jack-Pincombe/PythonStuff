import time, random


def buildArray(x):
    array = []
    for i in range(x):
        array.append(random.randint(0,x))
    return array

array = buildArray(1000)

def bubble(array):
    array = array
    iterations = 1
    while(iterations != 0):
        iterations = 0

        for i in range(len(array) -1):
            tmp = 0
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                iterations += 1

    return array

#print(bubble(array))

def quicks(array):
    array = array
    greater = []
    equal = []
    less = []
    if len(array) > 1:
        pivot = array[0]
        for i in array:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                less.append(i)
            else:
                equal.append(i)
        return quicks(less) + equal + quicks(greater)
    return array

print quicks(array)