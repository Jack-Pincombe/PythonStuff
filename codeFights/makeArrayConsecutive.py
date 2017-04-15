'''
this function will return the number of ints to make a list
consecutive
'''


def makeArrayConsecutive2(statues):
    x = sorted(statues)
    total = 0
    for i in range(len(x) - 1):
        if x[i + 1] - x[i] != 1:
            y = (x[i + 1] - x[i]) - 1
            total += y

    return (total)