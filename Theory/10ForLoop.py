# A for loop in Python is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)


# Lopping a String
for x in "Statement":
    print(x)                # Result: S t a t e m e n t


# The Break statement similar to while loop
for x in fruits:
    print(x)
    if x == "banana":
        break               # Result: apple banana
  

# The range() Function
for number in range(8):
    print(number)           # Rsult: 0 1 2 3 4 5 6 7

for x in range(2, 15, 3):   
    print(x)                  # Result: 2 5 8 11 14
else:
    print("Finally finished!")


# Nested Loops
numbers = [1, 2] 

for x in fruits:
    for y in numbers:
        print(x, y)
""" Result:
apple 1
apple 2
banana 1
banana 2
cherry 1
cherry 2
"""


# The pass statement
for x in [0, 1, 2]:
    pass