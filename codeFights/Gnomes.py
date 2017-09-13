
'''
taking an array and calculating how many ints need to be added to make it increment
'''

gnomes = [ 6,3,2,8,10]

#the correct answer should be 3 as we need 4,5,7 to make 2,3,4,5,6,7,8

def get(x):

    total = 0

    g = sorted(x)

    for i in range(len(g) - 1):
        difo = g[i + 1] - g[i]
        if  difo > 1:
            total += difo - 1

    return total


print(get(gnomes))
