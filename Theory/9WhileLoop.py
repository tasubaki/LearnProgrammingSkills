# Create While loop
number = 1

while number < 6:
    print(number)

    number += 1     # Result: 1 2 3 4 5


# The break statement
while number < 6:
    print(number)     

    if number==3:
        break
    
    number += 1    # Result: 1 2 3


# The continue statement
while number < 6:
    number += 1     

    if number==3:
        continue
    
    print(number)     # Result: 2 4 5 6     
else:
  print("Number is no longer less than 6")