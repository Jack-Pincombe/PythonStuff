aList = [1,3,5,6,8,9,10,12,34,56,78,456]
def recursiveBinarySearch(aList,  start,end,target):
    #aList = sorted(aList)

    if end-start+1 <= 0:
        return False
    else:
        midpoint = start + (end - start) // 2
        if aList[midpoint] == target:
            return midpoint
        elif aList[midpoint] != target and len(aList) == 1:
            return aList[midpoint]
        else:
            if target < aList[midpoint]:
                print(midpoint)
                return recursiveBinarySearch(aList, start, midpoint-1,target)
            else:
                print(midpoint)
                return recursiveBinarySearch(aList, midpoint+1, end,target)

print(recursiveBinarySearch(aList, 0, len(aList),1))
