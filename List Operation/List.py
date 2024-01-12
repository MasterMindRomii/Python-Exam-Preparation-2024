List = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 50, 40, 30, 20]
List2 = [12, 45, 64, 34, 78, 98]
List5 = [True, False, False, True]

print("Before Operation the list are:")
print("List: ", List)
print("List2: ", List2)
print("List3: ", List5)

print("\nOperations of list:\n")

# 1. Append an element
List.append(60)
print(List)

# 2. Shallow Copy of a existing list
List5 = List2.copy()
print(List5)

# 3. Extend (Addition of No. of elements)
List.extend(List2)
print(List)

# 4. Max no. in List
print(max(List))

# 5. Min no. in List
print(min(List))

# 6. Insert Method
List.insert(0, 70)
print(List)

# 7. Count Method
print(List.count(70))

# 8. Pop Method
print(List.pop(4))

# 9. Reverse List in Ascending Order
List.sort()
print(List)

# 10. Reverse List in descending Order
List.sort(reverse=True)
print(List)

# 11. Concatenation of list

List4 = List + List2
print(List4)

# 12. Remove an element - first occurence
List4.remove(70)
print(List4)

# 13. Length of list
print(len(List4))

# 14. Clear all elements
List4.clear()
print(List4)

# 15. Any() method
print(any(List5))

# 16. All() method
print(all(List5))

# 17. Index() Method
l=[10,34,5,6,765,78]
print(l.index(78,1,12))
print(l)


print("\nAfter Operations the list are:\n")
print("List: ", List)
print("List2: ", List2)
print("List3: ", List5)
print("List4: ", List4)
