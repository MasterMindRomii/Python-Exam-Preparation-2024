def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


x = (2, 3, 4, 5, 6, 7, 8, 9, 10)
y = tuple(map(Factorial, x))
print("The factorial of number is: ", y)
