nums = [12,43,253,2,323432,53,21,24,4,5,2,3,4,999]

def binarySearch(aList,target):
    #binary search algorithim
    aList.sort()

    if len(aList) == 0:
        return False
    else:
        m = len(aList) // 2  # gaining the midpoint
        if aList[m] == target:
            return True
        else:
            if target > aList[m]:
                return binarySearch(aList[m+1:],target)
            else:
                return binarySearch(aList[:m],target)

print binarySearch(nums,5)
