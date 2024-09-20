"""
Notes:
Parameters or Arguments?
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

# Create function
def my_function():
    print("Heel")


# Calling a function
my_function()                   # Result: Heel

# Arguments
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")             # Result: Emil Refsnes
my_function("Tobias")           # Result: Tobias Refsnes
my_function("Linus")            # Result: Linus Refsnes