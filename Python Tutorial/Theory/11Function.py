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


# Number of Arguments. not more, and not less.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")  # Result: Emil Refsnes


# Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus") # Result: The youngest child is Linus


# Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") # Result: The youngest child is Linus


# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") # Result: His last name is Refsnes


# Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")   # Result: I am from Sweden
my_function("India")    # Result: I am from India
my_function()           # Result: I am from Norway
my_function("Brazil")   # Result: I am from Brazil


# Passing a List as an Argument
"""
You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function.
"""
def my_function(food):
  for x in food:
    print(x, end=" ")

fruits = ["apple", "banana", "cherry"]

my_function(fruits)     # Result: apple banana cherry


# Return Value
def my_function(x):
  return x + 10

print(my_function(3))   # Result: 13


# Function Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result, end=" ")
  else:
    result = 0
  return result

tri_recursion(6)
"""
Diễn giải từng bước khi gọi tri_recursion(6):

    Bước 1: tri_recursion(6) được gọi:
        k = 6 nên chương trình tạm dừng tại dòng result = k + tri_recursion(k - 1), 
        nghĩa là nó chờ kết quả của tri_recursion(5).

    Bước 2: tri_recursion(5) được gọi:
        k = 5 nên chương trình tạm dừng tại dòng result = k + tri_recursion(k - 1), 
        chờ kết quả của tri_recursion(4).

    Bước 3: tri_recursion(4) được gọi:
        k = 4 và lại tạm dừng để chờ kết quả của tri_recursion(3).

    Bước 4: tri_recursion(3) được gọi:
        k = 3 và tạm dừng để chờ kết quả của tri_recursion(2).

    Bước 5: tri_recursion(2) được gọi:
        k = 2 và tạm dừng để chờ kết quả của tri_recursion(1).

    Bước 6: tri_recursion(1) được gọi:
        k = 1 và tạm dừng để chờ kết quả của tri_recursion(0).

    Bước 7: tri_recursion(0) được gọi:
        k = 0, điều kiện dừng xảy ra và trả về giá trị 0.
Tính toán ngược lại khi quay trở lại:

Sau khi hàm tri_recursion(0) trả về 0, 
chương trình bắt đầu quay ngược lại và tính toán ở từng bước trước đó:

    Quay lại bước 6: tri_recursion(1):
        Kết quả từ tri_recursion(0) là 0.
        Tính: result = 1 + 0 = 1.
        In 1.
        Trả về 1 cho tri_recursion(2).

    Quay lại bước 5: tri_recursion(2):
        Kết quả từ tri_recursion(1) là 1.
        Tính: result = 2 + 1 = 3.
        In 3.
        Trả về 3 cho tri_recursion(3).

    Quay lại bước 4: tri_recursion(3):
        Kết quả từ tri_recursion(2) là 3.
        Tính: result = 3 + 3 = 6.
        In 6.
        Trả về 6 cho tri_recursion(4).

    Quay lại bước 3: tri_recursion(4):
        Kết quả từ tri_recursion(3) là 6.
        Tính: result = 4 + 6 = 10.
        In 10.
        Trả về 10 cho tri_recursion(5).

    Quay lại bước 2: tri_recursion(5):
        Kết quả từ tri_recursion(4) là 10.
        Tính: result = 5 + 10 = 15.
        In 15.
        Trả về 15 cho tri_recursion(6).

    Quay lại bước 1: tri_recursion(6):
        Kết quả từ tri_recursion(5) là 15.
        Tính: result = 6 + 15 = 21.
        In 21.
"""