"""
Số hoàn thiện(hay là số hoàn chỉnh, số hoàn hảo) là một số nguyên dương mà 
tổng các ước nguyên dương của nó(số nguyên dương bị nó chia hết ngoại trừ nó) bằng chính nó.
Tìm tất cả số hoàn thiện trong phạm vi 1-1000
VD: 6 = 1 + 2 + 3( tổng các ước 1 + 2 + 3 = 6 => 6 là số hoàn thiện)
"""

number = int(input("Enter number: "))
sum = 0

while True:
    for x in range(1, number):
        if number%x == 0:
            sum += x

    if sum == number:
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")

    Question = input("Enter \"N\" to escape, or press another character to continue: ")

    if Question == "n" or Question == "N":
        print("Complete the program")
        break



# Print multiplication table exercises
for i in range(2,10):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print("-"*20)


"""
Cho một ma trận có kích thước NxN. Hãy vẽ hình chữ "N"
bởi kí tự "*" trên ma trân trận. 
"""
N = int(input("Enter N: "))

for row in range(N):
    for column in range(N):
        if column==0 or column==N-1 or row==column:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print(" ")