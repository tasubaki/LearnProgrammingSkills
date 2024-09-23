# Create dictionary. Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisDict1 = dict(name = "John", age = 36, country = "Norway")

print(thisDict) # Result: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(thisDict["brand"]) # Result: Ford
print(thisDict1)


# Duplicates Not Allowed
thisDict2 ={
    "year": 2000,
    "year": 2000,
}

print(thisDict2) # Result: {'year': 2000}


# Dictionary Length
print(len(thisDict)) # Result: 3    


# Access Dictionary Items
print(thisDict.get("model")) # Result: Mustang
print(thisDict.keys()) # Result: dict_keys(['brand', 'model', 'year'])

print(thisDict.values()) # Result: dict_values(['Ford', 'Mustang', 1964])

print(thisDict.items()) # Result: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# Check if Key Exists
if "model" in thisDict:
    print("Yes")


# Change Values
thisDict["year"] = 2018 # Result: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

thisDict.update({"year": 2020}) # Result: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# Adding Items
thisDict["color"] = "red"


# Removing Items
thisDict.pop("model") #Result: {'brand': 'Ford', 'year': 2020, 'color': 'red'}
thisDict.popitem() # Result: {'brand': 'Ford', 'year': 2020}. Remove last item
#del thisDict["model"] # Delete specified item
#thisDict.clear() # Result: {}

# Loop
for x in thisDict:
    print(x)           # Result: brand year
    print(thisDict[x]) # Result: Ford 2020

for x in thisDict.values():
    print(x) # Result: Ford 2020

for x, y in thisDict.items():
    print(x, y)
"""
Result:
brand Ford
year 2020
"""


# Copy a Dictionary
dictCopy = thisDict.copy()
dictCopy = dict(thisDict)


# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


# Add Nested Dictionaries
nestedDict = {
    "thisDict" : thisDict,
    "thisDict1" : thisDict1,
    "thisDict2" : thisDict2
}


# Access Items in Nested Dictionaries
print(nestedDict["thisDict"]["brand"]) # Result: Ford


# Loop Through Nested Dictionaries
for x, obj in nestedDict.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
"""
Result:
    thisDict
    brand: Ford
    year: 2020
    thisDict1
    name: John
    age: 36
    country: Norway
    thisDict2
    year: 2000
"""

