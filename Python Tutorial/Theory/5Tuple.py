# Create tuple. A tuple is a collection which is ordered and unchangeable.
thisTuple = ("apple", "banana", "cherry")
thistuple1 = tuple((1, 2, 3)) # Use the tuple() constructor to make a tuple.

print(thisTuple) # Result: ('apple', 'banana', 'cherry')

print(len(thisTuple)) # Result: 3

# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple)) # Result: <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # Result: <class 'str'>  


# Tuples are unchangeable. You can convert the tuple into a list, 
# change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # Result: ('apple', 'kiwi', 'cherry')

# Add items
y = list(thisTuple)
y.append("orange")
thisTuple = tuple(y) # Result: ('apple', 'banana', 'cherry', 'orange')

tupleAdd = ("blue",)

thisTuple += tupleAdd # Result: ('apple', 'banana', 'cherry', 'orange', 'blue')
print(thisTuple)

# Remove items
y = list(thisTuple)
y.remove("apple")
thisTuple = tuple(y) # Result: ('banana', 'cherry', 'orange', 'blue')
""" del thistuple

print(thistuple) #this will raise an error because the tuple no longer exists
 """


# Unpack Tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) # Result: apple
print(yellow) # Result: banana
print(red) # Result: cherry

(green, yellow, *red) = thisTuple

print(green) # Result: banana
print(yellow) # Result: cherry
print(red) # Result: ['orange', 'blue']

(green, *yellow, red) = thisTuple

print(green) # Result: banana
print(yellow) # Result: ['cherry', 'orange']
print(red) # Result: blue


# Multiply Tuples
myTupele = thistuple1 * 2 # Result: (1, 2, 3, 1, 2, 3)


# Tuples method
print(myTupele.count(1)) # Result: 2. dùng để đếm số lương giá trị 1

print(myTupele.index(2)) # Result: 1. Search for the first occurrence of the value 1, and return its position


print(myTupele)