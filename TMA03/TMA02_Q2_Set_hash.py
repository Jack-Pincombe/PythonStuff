#!/usr/bin/env python3

# for M269 TMA02 Question 2, The Open University, 2016
# version: 12 June 2016

class Set:
    """
    Implements an ADT to store an unordered collection of unique items.
    """
    
    def __init__(self):
        """
        Creates an empty Set.
        Complexity: constant
        """
        # represent a set as a hash table (Python dictionary)
        # the keys are the items and the value is always 1
        self.items = dict()
   
    def size(self):
        """
        Returns the size of self.
        Complexity: constant
        """
        return len(self.items)
    
    def has(self, item):
        """
        Returns True if item is in self, otherwise False.
        Complexity: constant
        """
        return item in self.items

    def add(self, item):
        """
        Assumes item is not in self and adds item to self. 
        Complexity: constant
        """
        assert not self.has(item)
        self.items[item] = 1
    
    def intersection(self, other):
        """
        Returns a new set with the common items of self and other.
        """
        common = Set()
        for item in self.items:
            if other.has(item):
                common.add(item)
        return common

# test borderline case of no items
empty = Set()
assert empty.size() == 0
assert not empty.has(1)

# test borderline case of one item
one = Set()
one.add(3)
assert one.size() == 1
assert not one.has(1)
assert one.has(3)

# test more items
more = Set()
more.add(1)
more.add(3)
more.add(-5)
assert more.size() == 3
assert not more.has(2)
assert more.has(1)

# intersecting any set with the empty set results in the empty set
assert empty.intersection(one).size() == 0
assert more.intersection(empty).size() == 0

# intersection is commutative: the order doesn't matter
moreWithOne = more.intersection(one)
oneWithMore = one.intersection(more)
assert moreWithOne.size() == oneWithMore.size()
assert moreWithOne.has(3) and oneWithMore.has(3)

# test empty intersection of non-empty sets
another = Set()
another.add(2)
assert another.intersection(more).size() == 0

print('Set implementation passed all tests')