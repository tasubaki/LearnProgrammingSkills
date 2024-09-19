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


print(thisDict)
