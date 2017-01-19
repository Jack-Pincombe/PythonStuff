#!/usr/bin/env python3

# for M269 TMA01 Question 3, The Open University, 2016
# version: 25 June 2016

# Jack Pincombe E5244151

# make sure the Bookcase class file is in the same folder as this file
from TMA01_Q3_Bookcase import Bookcase

# Part a.ii.

def findSpace(aBookcase):
    """
    Returns the row and column of a free position in aBookcase.
    
    """
    # obtaining rows and columns



    row = aBookcase.getRows()
    column = aBookcase.getColumns()
    
    # looping over each cell
    for i in range(row):
        for j in range(column):
            
            #checking cell to find if empty
            if aBookcase.isEmptySpace(i,j):
                return i , j
    
   
    
  

# Part b.ii.

def addItem(aBookcase, name, mediaType):
    """
    Returns False if aBookcase is full, otherwise returns True and 
    adds item of given name and mediaType to aBookcase.
    """
    # ensuring user inserts correct arguments
    assert len(name) > 0
    assert len(mediaType) > 0
    
    # Ensuring that there are empty spaces
    
    if aBookcase.getEmptySpaces() == 0:
        print("Bookcase is full")
        return False
    # taking arguments from function
    title = name
    media = mediaType
    # getting row and column lengths
    row = aBookcase.getRows()
    column = aBookcase.getColumns()
    
    # iterating throught the cells
    for i in range(row):
        
        for j in range(column):
            # finding empty space
            if aBookcase.isEmptySpace(i,j):
                
                # assigning name and filetype to cell
                aBookcase.setName(i,j,title)
                aBookcase.setType(i,j,media)
                
                # confirming files added with user
                return "Added"
                break

# Part c

def countItems(aBookcase, mediaType):
    """
    Returns how many items of given mediaType are in aBookcase.
    """
    assert len(mediaType) > 0
    
    media = mediaType
    # creating a counter
    count = 0
    
    # iterating through cells
    for i in range(aBookcase.getRows()):
        for j in range(aBookcase.getColumns()):
            
            # finding if both mediatypes match
            if aBookcase.getType(i,j) == media:
                
                #incrementing counter
                count += 1
                
    return count

# Tests

GAME = "video game"         # constants for the media types, to avoid typos
FILM = "film"
BOOK = "book"
SONG = "music"

# create two bookcases and check they're empty

tiny = Bookcase(1, 1)      # borderline case: smallest possible bookcase
small = Bookcase(2, 3)

assert tiny.getRows() == 1
assert tiny.getColumns() == 1
assert small.getRows() == 2
assert small.getColumns() == 3

assert tiny.isEmptySpace(0, 0)          # borderline case: first item
assert tiny.getEmptySpaces() == 1

assert small.isEmptySpace(1, 2)         # borderline case: last item
assert small.getEmptySpaces() == 2*3

# smallest bookcase stays empty

assert findSpace(tiny) == (0, 0)

# add to the other an item in 2nd shelf, 1st place

small.setName(1, 0, "Store Wars episode X")
small.setType(1, 0, FILM)

# check the resulting bookcases

assert small.getType(1, 0) == FILM
assert small.getEmptySpaces() == 2*3 - 1    # one space less
assert findSpace(small) != (1, 0)           # any other space is free

# add another item, in first position

small.setName(0, 0, "Angry Poultry")
small.setType(0, 0, GAME)

# check the resulting bookcase

assert findSpace(small) != (0, 0) and findSpace(small) != (1, 0)

print("findSpace passed all tests")

# there are 4 free spaces, so adding 2 items must succeed

spaces = small.getEmptySpaces()
assert addItem(small, "Algorhythms, date structures and compatibility", BOOK)
assert addItem(small, "Angry Poultry: The Pigs Strike Back", GAME)

# check the resulting bookcase: 2 spaces less

assert small.getEmptySpaces() == spaces - 2

print("addItem passed all tests")

# the previous tests only added 1 film, 1 book and 2 video games

assert countItems(small, FILM) == 1
assert countItems(small, BOOK) == 1
assert countItems(small, GAME) == 2
assert countItems(small, SONG) == 0

print("countItems passed all tests")