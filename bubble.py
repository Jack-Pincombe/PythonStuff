import random
import time

#just a simple bubble sort

def createArray(x):
    array = []
    for i in range(x):
        array.append(random.randrange(0,999999))
    return array

def bubble(array):
    option = array
    iterations = 0
    tmp = 0
    t = 1
    #array = createArray(option)
    while(t > 0):
        t = 0
        for i in range(len(array) - 1):
            if array[i]> array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
                t += 1
                iterations +=1
    print(array)
    print(str(iterations) + " number of iterations")

def quickSort(array):

    #array = createArray(1000)
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for i in array:
            if pivot < i:
                greater.append(i)
            elif pivot > i:
                less.append(i)
            else:
                equal.append(i)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return array


if __name__ == '__main__':
    array = createArray(10000)
    array1 = createArray(100000000)

    start = time.time()
    bubble(array)
    stime = time.time() - start
    print("Time taken = ", "%.4f " % stime , "seconds")

    start = time.time()
    print quickSort(array1)
    s1time = time.time() - start
    print("Time taken = ", "%.4f " % s1time, "seconds")


