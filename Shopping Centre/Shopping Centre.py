'''
Creating a simple shopping centre simulation
'''
import time

basket = {}

areas = ["Beer", "Dairy", "Veg"]

Beer = {
    "Erdinger" : 4,
    "Harp": 2.50,
    "Heinekin": 3
}

Dairy = {
    "Milk": 1,
    "Butter" : 0.50,
    "Creame": 1
}

Veg = {
    "Carrots": 0.25,
    "Potato": 1,
    "Turnup": 0.50
}
Basket = { }

'''
A method to print each of the menus
'''
def printMenu(x):
    num = 1
    for i in x:
        print(num,"->",i,'£',x[i])
        num += 1
    print(len(x) + 1 , '-> Go Back')



# function to allow the user to add items to basket
def options(x):
    chosen = ''

    while ( chosen != "quit" or chosen != 'back'):
        chosen = input('')
        if chosen == "1":

            print(x[int(chosen) - 1])
            print(Basket)

        elif chosen == '4':
            mainMenu()




def greeting():
    print("Welcome to ASDA")
    time.sleep(1)




def mainMenu():
    print("Which area would you like to view")

    for i in range(len(areas)):
        print(i + 1, '->' , areas[i])
        time.sleep(0.1)

    print(len(areas) + 1, "-> Basket")

    print("Enter the corresponding number")
    option = input("......")

    if int(option) > 3 or int(option) < 1:
        print("Please enter a valid number")
        mainMenu()

    elif int(option) == 1:

        printMenu(Beer)
        options(Beer)

    elif int(option) == 2:

        printMenu(Dairy)
        options(Dairy)
    elif int(option) == 3:

        printMenu(Veg)
        options(Veg)





def checkout(bask):
    pass




def __main__():
    greeting()

    mainMenu()

__main__()

