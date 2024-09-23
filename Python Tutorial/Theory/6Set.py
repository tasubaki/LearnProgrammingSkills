# Create Set. Set items are unordered, unchangeable, but you can remove items and add new items.
thisSet = {"apple", "banana", "cherry"}
thisSet1 = set((1,2,"aba"))

print(thisSet) # Result: {'banana', 'apple', 'cherry'}
print(thisSet1) # Result: {1, 2, 'aba'}


# Duplicates Not Allowed. The values True, 1 and False, 0 are treated as duplicates.
thisSet2 = {"apple", "banana", "cherry", True, 1, False, 0, 2}

print(thisSet2) # Result: {False, True, 2, 'cherry', 'apple', 'banana'}


# Get the Length of a Set
print(len(thisSet2)) # Result: 6


# Add Items
thisSet.add(6) # Result: {'banana', 6, 'cherry', 'apple'}

thisSet1.update(thisSet) # Result: {1, 2, 'aba', 'banana', 6, 'apple', 'cherry'}


# Remove Item
thisSet.remove("banana") # Result: {6, 'cherry', 'apple'}
thisSet.discard(6) # Result: {'cherry', 'apple'}
thisSet.pop() # Remove random
thisSet.clear() # Result: set()
# del thisSet. Delete full set


# Join Set
setJoin = {"thick"}

#thisSet = thisSet1.union(setJoin) # Result: {1, 2, 'aba', 'apple', 'banana', 6, 'cherry', 'thick'}. 
# Able Join multiple sets
thisSet = thisSet1 | setJoin # Result: {1, 2, 'aba', 'apple', 'banana', 6, 'cherry', 'thick'}
print(thisSet1.intersection(thisSet2)) # Result: {'cherry', 2, True, 'apple', 'banana'}. Keep ONLY the duplicates
print(thisSet1.difference(thisSet2)) # Result: {'aba', 6}
print(thisSet1.symmetric_difference(thisSet2)) # Result: {False, 6, 'aba'}
