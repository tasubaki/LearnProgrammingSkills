"""
Nhập : Họ tên học sinh, Môn, Điểm
In ra màn hình học sinh được chọn nếu điểm môn dự thi từ 7 điểm trở lên.
Lặp lại với học sinh khác cho đến khi gõ ký tự 'N' thì kết thúc.
"""

while True:
    Student = input("Enter name: ")
    Objects = input("Enter object: ")
    Score = float(input("Enter score: "))

    print(f"Student {Student} took the {Objects} exam and got a score of {Score}.")

    if Score >= 7:
        print("Pass")
    else:
        print("Not pass")

    Question = input("Enter \"N\" to escape, or press another character to continue: ")

    if Question == "n" or Question == "N":
        break
