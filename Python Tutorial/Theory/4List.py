# Create List
thislist = ["apple", "banana", "cherry", "kiwi", "melon", "mango"]

print(len(thislist)) # Result: 3
print(thislist[1]) # Result: banana
print(thislist[3:]) # Result: ['kiwi', 'melon', 'mango']


# Check if Item Exists
if "apple" in thislist:
    print("True")


# Change item
thislist[1] = "blackcurrant"

thislist[1:3] = [1, 2] # Change a Range of Item 


# Insert Items
thislist.insert(2, "watermelon")


# Append Items
thislist.append(3) # Add to end of list


# Extend list
thislist2 = [4, 5]

thislist.extend(thislist2) # Add 2 list


# Remove Specified Item
thislist.remove(1) # Delete by value
thislist.pop(1)    # Delete by index
del thislist[0]    # Delete by index
#thislist.clear()   # Delete full list


# Loop Through a List
for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])

while i < len(thislist):
  print(thislist[i])
  i = i + 1


# Copy list
newlist = [x for x in range(len(thislist))] # Result: [0, 1, 2, 3, 4, 5, 6]
mylist = thislist.copy() # Result: [2, 'kiwi', 'melon', 'mango', 3, 4, 5]
mylist1 = list(thislist) # Result: [2, 'kiwi', 'melon', 'mango', 3, 4, 5]
mylist2 = thislist[:]    # Result: [2, 'kiwi', 'melon', 'mango', 3, 4, 5]


# Sort list
# thislist.sort() sắp xếp theo thứ tự alpha, số từ bé đến lớn
# thislist.sort(reverse = True) sắp xếp giảm dần
# thislist.reverse() sắp xếp giảm dần


# Join Two Lists
listjoin = [10, 11, 12]

mylist3 = mylist2 + listjoin # [2, 'kiwi', 'melon', 'mango', 3, 4, 5, 10, 11, 12]

for x in listjoin:
  mylist3.append(x) # [2, 'kiwi', 'melon', 'mango', 3, 4, 5, 10, 11, 12, 10, 11, 12]

mylist3.extend(listjoin) # [2, 'kiwi', 'melon', 'mango', 3, 4, 5, 10, 11, 12, 10, 11, 12, 10, 11, 12]
