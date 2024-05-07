# This script performs basic arithmetic operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Basic testing of the functions
print(add(15, 5))
print(subtract(15, 5))
print(multiply(15, 5))
print(divide(15, 0))  # Proper division by zero check
