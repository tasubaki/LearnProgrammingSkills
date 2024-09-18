import sys

print(sys.version) # result: 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]
print("hello") # result: hello

def helloWorld(printer):
    printer("hi abc")

helloWorld(print) # result: hi abc


def calculate(printer):
    print("1 + 1 =", 1+1)

calculate(print) # result: 1 + 1 = 2


def cal(length, width):
    area = length*width
    perimeter = (length + width)*2
    
    print("Area =", area)
    print("Perimeter =", perimeter)
    print(f"Area = {area}")
    print(f"Perimeter = {perimeter}")

cal(2,5) # result: Area = 10 , Perimeter = 14


class Rectangle:
    def __init__(self, length, width):
        # Set object properties
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

rect = Rectangle(2, 5) # Init object from Rectangle class
print("Area =", rect.area())
print("Perimeter =", rect.perimeter())


area = lambda length, width: length * width # lambda function multiplies two numbers.
perimeter = lambda length, width: (length + width) * 2

print("Area_Lambda =", area(2, 5))
print("Perimeter_Lambda =", perimeter(4, 8))