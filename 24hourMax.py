

def solution(A,B,C,D):
    #return as a string
    time = ""
    total = []
    total.append(A)
    total.append(B)
    total.append(C)
    total.append(D)

    max_hour = 24
    max_minute = 60

    tmpHour = 0
    tmpMinute = 0
    x = 0
    y = 0

    for i in range(len(total)):
        for j in range(len(total)):
            if total[i] > 9 or total[j] > 9:
                return "This will not work"

            elif int(str(total[i]) + str(total[j])) < max_hour and int(str(total[i]) + str(total[j])) > tmpHour and i != j:
                tmpHour = int(str(total[i]) + str(total[j]))
                x = int(str(total[i]))
                y = int(str(total[j]))

    if tmpHour == 0:
        return "This will not work"

    total.remove(x)
    total.remove(y)

    for i in range(len(total)):
        for j in range(len(total)):
            if int(str(total[i]) + str(total[j])) < max_minute and int(str(total[i]) + str(total[j])) > tmpMinute and i != j:
                tmpMinute = int(str(total[i]) + str(total[j]))

    if tmpMinute == 0:
        tmpMinute = "00"
    elif tmpMinute > 59:
        return "This will not work"

    return(str(tmpHour) + ':'+ str(tmpMinute))


print(solution(5,2,4,3))
print(solution(9,9,9,9))
print(solution(2,3,0,0))
print(solution(1,34,5,4))


