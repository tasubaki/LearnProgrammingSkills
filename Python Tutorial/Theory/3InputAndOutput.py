# Input from keyboard
name = input("Enter: ")  
print("Hello " + name)

number1, number2 = input("Enter 2 numbers separated by spaces: ").split()

print(f"Number1 = {number1}, number2 = {number2}")

def input_name(name):
    print("Hello", name)

name1 = input("Enter: ")

input_name(name1)


# Output printing methods
def input_name(name,age):
    print("In 15 years, age of", name, "will be", str(age + 15)) # Convert age data type from int to str
    print("In 15 years, age of " + name + " will be "+ str(age + 15))
    print(f"In 15 years, age of {name} will be {str(age + 15)}")
    print("In 15 years, age of {} will be {}".format(name, str(age + 15)))

name = input()
age = int(input())

input_name(name, age)   
