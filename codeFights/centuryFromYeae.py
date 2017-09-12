'''
Code fights challenge to determine the century of which a given year
is in
'''

def centuryFromYear(year):
    x = str(year)

    if x[1:] == "00":
        if len(x) == 3:
            return int(x[0])
        return int(x[:2])

    elif x[2:] == "00":
        return(int(x[:2]))

    elif len(x) <= 2:
        return 1

    elif len(x) <= 3:
        return int(x[:1]) + 1

    else:
        x = int(x[:2])
        return(x + 1)


def __main__():
    year = input("Please enter a year: ")
    print(centuryFromYear(year))

__main__()