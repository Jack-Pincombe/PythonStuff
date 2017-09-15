import time
import locale
result = locale.setlocale(locale.LC_ALL, 'en_GB.UTF-8')


beer = [
    ["Erdinger", 3.00],
    ["Harp", 3.00],
    ["Tennents", 2.50]
]

dairy = [
    ["Milk", 1.00],
    ["Cheese", 2.00],
    ["Cream", 3.00]
]

veg = [
    ["Carrots", 0.10],
    ["Pumpkin", 2.00 ]
]
basket = [

]

def space(x):
    for i in range(x):
        print("\n")

def intro():
    print("Hello and welcome to the store")

def whichAisle():
    print("-----------------------------------------------------------\n"
          "-----------------------------------------------------------\n"
          "-----------------------------------------------------------\n")


    options = [ "1 -> Beer","2 -> Dairy", "3 -> Veg","4 -> Checkout","5 -> Leave" ]

    for i in options:
        print(i)
    aisle = input("Please select an aisle ")


    if aisle == '4':
        returnBasket()

    elif aisle == '5':
        leave()

    elif int(aisle)  > len(options) or aisle.isdigit() == False:
        space(2)
        print("Please enter a valid option")
        time.sleep(2)
        space(10)
        whichAisle()
    else:
        printMenu(aisle)

def leave():
    print("Good Bye")
    quit()

def add(aisle):

    if aisle == '4':
        return whichAisle()


    elif aisle == '1':
        try:
            chosen = input('Add -> ')
            val = int(chosen)

        except ValueError:
            print("That is not a valid option")

        if int(chosen) > len(beer) + 1 or int(chosen) < 0:
            print("Please select a valid option 1")
            time.sleep(2)
            whichAisle()
        space(2)
        print("Item has been added")
        basket.append(beer[int(chosen) - 1])
        return whichAisle()

    elif aisle == '2':
        chosen = input('Add -> ')
        if int(chosen) > len(dairy) + 1 or int(chosen) < 0:
            print("Please select a valid option 2")
            time.sleep(2)
            whichAisle()
        space(2)
        print("Item has been added")
        basket.append(dairy[int(chosen) - 1])
        return whichAisle()

    elif aisle == '3':
        chosen = input('Add -> ')
        if int(chosen) > len(veg) + 1 or int(chosen) < 0:
            print("Please select a valid option 3")
            time.sleep(2)
            whichAisle()
        space(2)
        print( "Item has been added")
        basket.append(veg[int(chosen) - 1])
        return whichAisle()



    printMenu(aisle)

def returnBasket():
    for i in basket:
        print(i)

    total = 0
    for i in range(len(basket)):
        total += basket[i][1]

    print("Your total is " ,locale.currency(total))



def printMenu(aisle):


    if aisle == "1":
        for i in range(len(beer)):
            print(i + 1 , ' -> ',beer[i])
        print(len(beer) + 1 , ' -> Go back')
        add('1')

    elif aisle == '2':
        for i in range(len(dairy)):
            print(i + 1 , ' -> ',dairy[i])
        print(len(dairy) + 1, ' -> Go back')
        add('2')

    elif aisle == '3':
        for i in range(len(veg)):
            print(i + 1 , ' -> ',veg[i])
        print(len(veg) + 1, ' -> Go back')
        add("3")


def __main__():
    intro()
    whichAisle()

__main__()