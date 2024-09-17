import sys

print(sys.version) # 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]

print("hello")

def helloWorld(printer):
    printer("hi abc")

helloWorld(print) # hi abc

def calculate(printer):
    print("1 + 1 =", 1+1)

calculate(print) # 1 + 1 = 2

def cal(length, width):
    area = length * width
    perimeter = (length + width) * 2
    print("Area =", area)
    print("Perimeter =", perimeter)

cal(2,5) # Area =10 , Perimeter =14