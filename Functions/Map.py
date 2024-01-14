# Example 1
def square(n):
    return n * n


x = [10, 20, 30, 40, 50]
y = list(map(square, x))
print(y)

# Example 2
def cube(n):
    return n * n * n


x = [12, 13, 14, 15, 16]
y = list(map(cube, n))
print(y)

# Example 3
def Even_Number(n):
    if n % 2 == 0:
        print(n, " Yes,it is an even number")
    else:
        print(n, " Not,it is not an even number")


x = (12, 17, 22, 19, 16, 18, 76, 345, 657, 98, 11)
y = tuple(map(Even_Number, x))
print(y)


