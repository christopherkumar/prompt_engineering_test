# Calculator for addition, subtraction, multiplication, and division

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

# Usage of functions
print(add(20, 10))
print(subtract(20, 10))
print(multiply(20, 10))
print(divide(20, 0))
