#!/usr/bin/env python3

# for M269 TMA02 Question 3, The Open University, 2016
# version 19 December 2016

# The standard insertion sort function and the (iterative) binary search
# functions in this file are based on similar code in
# Introduction to Data Structures and Algorithms in Python
# by Bradley N. Miller and David L. Ranum (c)2005.

import random
import time
   
# Question 1 (a)
# --------------
 
# Don't change this function
def linearInsertionSort(aList):
    '''
    Standard insertion sort (using linear search)
    '''
    start = time.time()
    for currentPosition in range(1, len(aList)):
        currentValue = aList[currentPosition]
        position = currentPosition
        while position > 0 and aList[position - 1] > currentValue:
            aList[position] = aList[position - 1]
            position = position - 1
        aList[position] = currentValue
    elapsed = time.time() - start
    print('linearInsertionSort:', len(aList), 'items =', "%.4f" % elapsed,
          'seconds')


# Don't change this function
def testSortPerformance(sortFunction, noOfSamples):
    '''
    Run tests to check Big-O performance of specified list sorting
    function 'sortFunction'.
    Note this uses an advanced feature of Python that allows functions
    to be passed as arguments
    '''
    print()
    print('Testing sorting performance at different sample sizes')
    print()
    
    sampleSize = 10
    for sample in range(noOfSamples):

        # Create an unsorted list of random integers 
        testList = []
        for i in range(sampleSize):
           testList.append(random.randrange(0, sampleSize))
        
        sortFunction(testList)
        
        sampleSize = sampleSize * 2     # the next sample has double the size

# Change the number below to choose an appropriate number of test samples. 
# Bear in mind that for more than a few samples,
# the running time required could be substantial,
# so it is best to start with a small number of samples and see how it goes.
noOfSamples = 5
#testSortPerformance(linearInsertionSort, noOfSamples)


# Question 1 (b)
# --------------


# Add your code for this function
# You may find it helpful to consult the M&R textbook 
# and the iterativeBinarySearch function provided further below
def recursiveBinarySearch(aList,  first,last,target):
    if last-first+1 <= 0:
        return last + 1
    else:
        midpoint = first + (last - first) // 2
        if aList[midpoint] == target:
            return midpoint
        else:
            if target < aList[midpoint]:
                return recursiveBinarySearch(aList, first, midpoint-1,target)
            else:
                return recursiveBinarySearch(aList, midpoint+1, last,target)








    '''
    Preconditions: aList is in ascending order
                   0 <= first < len(aList); last < len(aList)
    Searches for 'target' in sorted list 'aList' between indices 'first' and 'last'
    If 'target' present, returns the corresponding list index
    If 'target' not present, returns the list index of the item immediately
      above this in value, returning last+1 if 'target' is higher in value than
      all items in the list
    '''
    pass

# Don't change this function
def testBinarySearch(search):
    '''
    Test the binary search function passed as the argument called 'search'
    Note this uses an advanced feature of Python that allows functions
    to be passed as arguments.
    The output may be useful in debugging your binary search function.
    '''
    testList = [2, 8, 17, 42, 79, 85]

    listSize = len(testList)

    print()
    print('Checking output for values that are present:')
    for i in range(0, listSize):
      target = testList[i]
      foundAt = search(testList, 0, listSize-1, target)
      if foundAt == i:
        print('Found value ', target, ' at index ', foundAt,
              ' as expected')
      else:  
        print('Found value ', target, ' at index ', foundAt,
              ' instead of expected value', i)

    print()
    print('Checking output for values that are not present:')
    for i in range(0, listSize):
      target = testList[i]+1  # no consecutive integers in test list
      foundAt = search(testList, 0, listSize-1, target)
      if foundAt == i+1:
        print('Searching for value ', target, ' returned index ',
              i+1, ' as expected')
      else:  
        print('Searching for value ', target, ' returned index ',
              foundAt, ' instead of expected value', i+1)
    
    print()
    print('Checking output for value that precedes all present:')
    target = testList[0]-1
    foundAt = search(testList, 0, listSize-1, target)
    if foundAt == 0:
        print('Searching for value ', target, ' returned index ',
              foundAt, ' as expected')
    else:  
        print('Searching for value ', target, ' returned index ',
              foundAt, ' instead of expected value 0')
       
# Run tests on your function recursiveBinarySearch
print()
print('Testing recursive binary search')
testBinarySearch(recursiveBinarySearch)


# Question 1 (c)
# --------------


# Don't change this function
def iterativeBinarySearch(aList, first, last, target): 
    '''
    Alternative implementation of binary search
    For use in Q1(c) only if Q1(b) not completed
    Preconditions: aList is in ascending order
                   0 <= first < len(aList); last < len(aList)
    '''
    found = False
      
    while first <= last and not found: 
        midpoint = (first + last) // 2 
        if aList[midpoint] == target: 
            found = True 
        else: 
            if target < aList[midpoint]: 
                last = midpoint-1 
            else: 
                first = midpoint+1 
       
    if first > last:        # i.e. target not found
        return first
    else:
        return midpoint     # i.e. target found


# Add your code for this function
def binaryInsertionSort(aList):
    '''
    Insertion sort (using binary search)
    '''
    start = time.time()
    pass
    elapsed = time.time() - start
    print('binaryInsertionSort: ', len(aList), 'items =', "%.4f" % elapsed,
          'seconds')

# Test with the same number of samples 
#testSortPerformance(binaryInsertionSort, noOfSamples)

