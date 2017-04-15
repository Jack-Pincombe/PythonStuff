'''
To return true if possible of making list ordered by removing one integer
'''


def almostIncreasingSequence(sequence):
    x = sequence
    return (almostInc(x, 0))


def almostInc(array, y):
    total = y
    x = array

    if len(x) == 1:
        return True
    else:
        for i in range(len(x) - 1):

            if i == 0 and x[i + 1] < x[i]:
                del x[i]
                total += 1
                return almostInc(x, total)
            elif x[i] > x[i + 1] and x[i + 1] > x[i - 1] and i > 0:
                del x[i]
                total += 1
                return almostInc(x, total)
            elif x[i + 1] <= x[i]:
                del x[i + 1]
                total += 1
                return almostInc(x, total)

    if total == 1 or total == 0:
        return True
    else:
        return False