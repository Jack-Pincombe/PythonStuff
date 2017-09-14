
class Item(object):

    def __init__(self,itemName,itemPrice):
        self.itemName = itemName
        self.itemPrice = itemPrice

    def getName(self):
        return self.itemName

    def getPrice(self):
        return self.itemPrice
    def setPrice(self,cost):
        self.itemPrice = cost
        return self.itemPrice, " Now costs " , cost

    def setPrice(self,name):
        self.itemName = name

class Basket(object):
    def showcart(self):
        return self

class User(object):

    def __init__(self,name):
        self.name = name

    def AddCart(self):