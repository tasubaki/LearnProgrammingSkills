""" 
Nhập vào từ bàn phím thời gian về đích của 3 vận động viên(tính bằng giây).
Xuất ra màn hình thời gian về đích dbt là điểm trung bình cộng thời gian về đích của 3 vận động viên
"""
# Solution 1
athlete1 = float(input("Athlete time(s) 1:"))
athlete2 = float(input("Athlete time(s) 2:"))
athlete3 = float(input("Athlete time(s) 3:"))

#dbt = (athlete1 + athlete2 + athlete3)/3

print("dbt =", str((athlete1 + athlete2 + athlete3)/3))


# Solution 2
times = input("Enter the times of 3 athletes, separated by spaces: ").split()
athletes = list(map(float, times))

dbt = sum(athletes) / len(athletes)

print("dbt =", round(dbt, 2))


# Solution 3
athletes = []
for i in range(3):
    time = float(input(f"Enter time of athlete {i+1} (seconds): "))
    athletes.append(time)
#athletes = [float(input(f"Enter time of athlete {i+1} (seconds): ")) for i in range(3)]

dbt = sum(athletes) / len(athletes)

print(f"dbt = {round(dbt, 2)}")

