# Dictionary functions in python

Dict1 = {1: "India", 2: "USA", 3: "England", 4: "Australia", 5: "Hong-kong"}
Dict2 = {1: "Delhi", 2: "Haryana", 3: "Punjab", 4: "Gujrat", 5: "Bihar"}
Dict3 = {1: 12, 2: 13}

print("Before Operation the Dictionary are:")
print("Dict1: ", Dict1)
print("Dict2: ", Dict2)
print("Dict3: ", Dict3)
print("\nOperations of Dictionary:\n")

# 1. len()-
print(len(Dict1))
print(len(Dict2))
print(len(Dict3))

# 2. Get() Method -
res = Dict1.get(1)
print(res)

res1 = Dict2.get(3)
print(res1)

res2 = Dict3.get(4)  # None Expected
print(res2)

# 3. Keys()-
print(Dict1.keys())
print(Dict2.keys())
print(Dict3.keys())

# 4. Values()-
print(Dict1.values())
print(Dict2.values())
print(Dict3.values())

# 5.Item()-
New_Dict = Dict1.items()
print(New_Dict)

New_Dict2 = Dict2.items()
print(New_Dict2)

New_Dict3 = Dict3.items()
print(New_Dict3)

# 6.Fromkeys()-
d1 = dict.fromkeys("Happy New Year", 12)
print(d1)

d2 = dict.fromkeys([12, 13, 14, 15], 200)
print(d2)

d3 = dict.fromkeys(("romi", "harsh", "rahul"), "kumar")
print(d3)

# 7. SetDefault()-
d4 = Dict1.setdefault(6, "Poland")
print(d4)

d5 = Dict2.setdefault(6, "Hyderabad")
print(d5)

d6 = Dict3.setdefault(3, 12)
print(d6)

d7 = Dict3.setdefault(4)
print(d7)

# 8. pop()-
Dict1.pop(4, "Deleted Successfully")
print(Dict1)

Dict2.pop(12, "Key Not Available :(")
print(Dict2)

Dict3.pop(3, "Deleted Successfully")
print(Dict3)

# 9. Sorted()-
d8 = sorted(Dict1)
print(d8)

d9 = sorted(Dict2)
print(d9)

d10 = sorted(Dict3)
print(d10)

d11 = sorted(Dict2, reverse=True)
print(d11)

# 10. Change/Update Dictionary Items-
Dict1[2] = "Dubai"
print(Dict1)

# 11. Copy()-
d12 = Dict1.copy()
print(d12)

# 12. Nested Dictionary -
Nested_Dict = {
    "A": "APPLE",
    "B": "BALL",
    "C": "CAT",
    "NEXT": {"D": "DOG", "E": "ELEPHANT", "F": "FISH"},
}
print(Nested_Dict["NEXT"]["F"])
print(Nested_Dict["NEXT"]["E"])

# 13.Delete elements from a Nested Dictionary-
del Nested_Dict["NEXT"]["F"]
print(Nested_Dict)

# 14. to delete dictionary from a nested dictionary
del Nested_Dict["NEXT"]
print(Nested_Dict)

# 15. Delete dictionary
del Dict1
print(Dict1)

# 16. Update Dictionary - Merge two dictionary
d13=Dict1.update(Dict2)
print(d13) #Return None

print("After Operation the Dictionary are:")
print("Dict1: ", Dict1)
print("Dict2: ", Dict2)
print("Dict3: ", Dict3)
