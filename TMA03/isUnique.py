''' Return True if a string has all unique characters'''

word = "abfgbaidgfsgbksafjgasfbjgasgibaskgj"

def brute(x):
    ''' Brute force using two for loops
        runtime would be O(n^2)
    '''
    x = x.lower()
    print x
    for i in range(len(x)):
        for j in range(i+1, len(x)-1):
            if x[i] == x[j +1]:
                return "This item is not unique"

    return "this item is unique"

print brute(word)