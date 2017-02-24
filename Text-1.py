lT = 1
tT = 1
tN = 2

x = int(input("Input: "))

while tN < x:
    nT = lT + tT
    lT = tT
    tT = nT
    tN += 1
    
    print("Value of ", x, 'is', nT)
    
    