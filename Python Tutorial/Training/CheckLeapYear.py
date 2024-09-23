"""
Viết chương trình nhập vào 1 năm dương lịch, kiểm tra năm đó có phải năm nhuận hay không?
Đếm số ngày trong tháng.
"""

year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Solution 1 use if...elif
if (year%4==0 and year%100!=0) or year%400==0:
    if month==1 or month==3 or month==5 or month ==7 or month==8 or month==10 or month==12:
    #if month in (1, 3, 5, 7, 8, 12):
        print(f"{year} is a leap year and {month} has 31 days!")
    elif month==4 or month==6 or month==9 or month==11:
        print(f"{year} is a leap year and {month} has 30 days!")
    else:
        print(f"{year} is a leap year and {month} has 29 days!")
else:
    if month==1 or month==3 or month==5 or month ==7 or month==8 or month==10 or month==12:
        print(f"{year} is not a leap year and {month} has 31 days!")
    elif month==4 or month==6 or month==9 or month==11:
        print(f"{year} is not a leap year and {month} has 30 days!")
    else:
        print(f"{year} is not a leap year and {month} has 29 days!") 


# Solution 2 use list
# Check leap year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# List day in month
days_in_month = [31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(f"{year} is {'a leap' if is_leap else 'not a leap'} year and month {month} has {days_in_month[month - 1]} days.")