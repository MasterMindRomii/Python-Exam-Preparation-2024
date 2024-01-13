# Example of a built-in function
length = len("Hello, World!")
print(length)

# Example of a user-defined function
def add(x, y):
    return x + y

result_user_defined = add(3, 5)
print(result_user_defined)

# Example of an anonymous function (lambda function)
add_lambda = lambda x, y: x + y
result_lambda = add_lambda(3, 5)
print(result_lambda)

# Example of a recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result_recursive = factorial(5)
print(result_recursive)
