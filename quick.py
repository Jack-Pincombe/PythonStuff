import random
import time


def createArray(x):
    array = []
    for i in range(x):
        array.append(random.randrange(0,x))
    return array


array = createArray(1000000)

def quickSort(array):

    #array = createArray(1000)
    less = [ ]
    equal = [ ]
    greater = [ ]
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
    start = time.time()
    print(quickSort(array))
    stime = time.time() - start
    print("Time taken = ", "%.4f " % stime , "seconds")
