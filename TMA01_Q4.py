# for M269 TMA01 Q4, The Open University, 2016
# version: 25 June 2016

# Jack Pincombe E5244151

from TMA01_Q4_MString import MString

def concatenate (first, second):
    for i in range(second.length()):
        first.addChar(second.getChar(i))
    return first





assert concatenate(MString("good"), MString("morning!")).toString() == "goodmorning!"
assert concatenate(MString("Open"), MString("University")).toString() == "OpenUniversity"
assert concatenate(MString("United"), MString("Kingdom")).toString() == "UnitedKingdom"
# add 2 tests here, in the same format
print("concatenate passed all tests")
