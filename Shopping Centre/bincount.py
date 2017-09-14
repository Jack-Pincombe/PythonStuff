'''
Given two lists of ints

return a list containing the difference
'''

def array_diff(a, b):
    #your code here
    for i in a:
        for j in b:
            if i == j:
                delet(a,i)
                delet(b,j)
                return array_diff(a,b)
    q = a + b
    return q


def delet(list, item):
    for i in list:
        if i == item:
            list.remove(item)
            return list



print(array_diff([1,2,2,2,3],[2]))