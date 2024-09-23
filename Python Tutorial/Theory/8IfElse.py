number = 8
number1 = 2
number2 = 2

if number < number1:
    print("number < number1")
elif number == number2: # If statement 1 is false, the action in this statement will be performed.
    print("number = number2")
else:
    print("number > number1") # The else keyword catches anything which isn't caught by the preceding conditions.

if number > number1 and number1 == number2:
    print("Yes")

if number == number1 or number1 == number2:
    print("Yes1")

if not number == number1:
    print("NOT")


if number2 > number1: #if statements cannot be empty, put in the pass statement to avoid getting an error.
  pass