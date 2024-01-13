t1 = (2, 4, 5, 6, 7, 8, 4, 3)
t2 = (12,)
t3 = (12, 45, 654, 324, 23)

print("Before Operation the tuples are:")
print("List: ", t1)
print("List2: ", t2)
print("List3: ", t3)

print("\nOperations of tuple:\n")

# 1. Length of tuple
print(len(t1))
print(len(t2))
print(len(t3))

# 2. Concatenation of tuple
t4 = t1 + t2 + t3
print(t4)

# 3. Repititon
print(t1 * 3)
print(t3 * 4)

# 4. MemberShip - in & not-in
print(5 in t1)
print(5 in t2)

# 5. Min & Max
print(max(t1))
print(min(t1))

# 6. Count()
print(t1.count(4))

# 7. Index()
print(t1.index(4,1,5))

# 8. Sorted()
print(sorted(t1))

# 9. Sum()
print(sum(t1))

# 10. Tuple()

l=['A','E','I','O','U']
tup=tuple(l)
print(tup)

# 11. Delete tuple 
del tup
print(tup)

# 12.Change mutable item in a tuple

t=(1,[2,3,4,5,6],3,7,8,9)
t[1][1]=34
print(t)

print("\nAfter Operations the tuples are:\n")
print("List: ", t1)
print("List2: ", t2)
print("List3: ", t3)
