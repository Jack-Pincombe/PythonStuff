import random

def quickSearch(list,left,right,k):

    if left == right:
        return list[left]

    split = partition(list, left, right)

    length = split - left + 1

    if length == k:
        return list[split]
    elif k < length:
        return quickSearch(list,left, split - 1, k)
    else:
        return quickSearch(list, split + 1, right, k - length)

def partition(list,left,right):

    pivot = list[left]
    leftMark = left + 1
    rightMark = right

    while True:
        while leftMark < right and list[leftMark] < pivot:
            leftMark += 1

        while rightMark > left and list[right] > pivot:
            rightMark -= 1

        if leftMark > rightMark:
            break
        else:
            temp = list[leftMark]
            list[leftMark] = list[rightMark]
            list[rightMark] = temp


    temp = list[left]
    list[left] = list[rightMark]
    list[rightMark] = temp

    return(rightMark)

def main():
    list = []

    for x in range(0,10):
        list.append(random.randint(1,1000))

    print(list)
    print(quickSearch(list, 0, len(list) - 1 , 8))

if __name__ == "__main__":
    main()