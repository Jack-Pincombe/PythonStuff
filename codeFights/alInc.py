'''
make a program to return bool if one number can be removed to make it incremental
'''

example1 = [1,3,2,1]
example2 = [1,2,1]
example3 = [1,2,1,2]

def almostIncreasingSequence(sequence):
    count = 0

    for i in range( len(sequence) - 1 ):

        if sequence[i] > sequence[i + 1]:
            count += 1

        if count > 1:
            return False

    return True

print(almostIncreasingSequence(example1))
print(almostIncreasingSequence(example2))
print(almostIncreasingSequence(example3))

