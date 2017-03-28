sequence = [1,2,3,4,3,5]

def almostInc(array,y):
    total = y
    x = array

    if len(x) == 1:
        return True
    else:
        for i in range(len(x) - 1):
            if x[i+1] < x[i]:
                del x[i+1]
                total += 1
                print x
                return almostInc(x,total)


print almostInc(sequence,0)