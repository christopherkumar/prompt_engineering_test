# Calculator script with basic arithmetic functions

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero error"
    return x / y

# Testing the functions
print(add(50, 25))
print(subtract(50, 25))
print(multiply(50, 25))
print(divide(50, 0))  # Handles division by zero
