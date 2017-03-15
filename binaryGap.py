
def binaryGap(n):
    x = bin(n)[2::]
    return count1(x)




def count1(x):
    print(x)
    x = str(x)
    print(x)

    y = len(x)
    i = 0
    tmp = 0
    count = 0
    while i < y - 2:

        if x[i] == "1" and x[i + 1] == "0":
            count += 1
            tmp += 1

        elif x[i] == "0" and x[i + 1] == "0":
            count += 1
            tmp += 1

        elif x[i] == "0" and x[i + 1] == "1":
            tmp = 0

        elif tmp > count:
                count = tmp


        i += 1
    return count




print(binaryGap(4856))