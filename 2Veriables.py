# Creating Variables
num_integer = 8 
num_float = 8.88888
string_var = "Hi Code"

print(num_integer)
print(num_float)
print(string_var)

var = 8 # var is of type int
var = "Hello " +"titi" # var is now of type str

print (var) # Result: Hello titi; Auto change data type and get last value


# Casting
number = int(8) # number will be 3
number1 = float(8) # number will be 3.0
number2 = str(8) # number will be '3'
fruits = ["apple", "banana", "cherry"] # ['apple', 'banana', 'cherry']
tuple = ('Apple', 16, True) # ('Apple', 16, True)
dictionary = {"Phone": "Apple", "Version": 16, "Port": True} # {'Phone': 'Apple', 'Version': 16, 'Port': True}

print(type(number)) # Result: <class 'int'>
print(type(number1)) # Result: <class 'float'>
print(type(number2)) # Result: <class 'str'>
print(type(fruits)) # Result: <class 'list>
print(type(tuple)) # Result: <class 'tuple'>
print(type(dictionary)) # Result: <class 'dict'>


name = "Thick"
date_of_birth = 2024
print("Name: " + name)
print("Date of birth: " + str(date_of_birth)) # convert data type before concatenating strings + numbers


x = "awesome" # Global variables

def myfunc():
  x = "fantastic" # Local variables
  print("Python is " + x) # Result: fantastic

myfunc()

print("Python is " + x) # Result: awesome


# Check string
txt = "The best things in life are free!"

print("free" in txt) # Result: True
print("expensive" not in txt) # Result: True


# Slicing Strings
text = "Hello, World!"

print(text[2:5]) # Result: llo
print(text[5]) # Result: ,
print(text[-5:-2]) # Result: orl
