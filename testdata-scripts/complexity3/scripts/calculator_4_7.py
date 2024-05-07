# A comprehensive calculator that can do addition, subtraction, multiplication, and division.

def add(x, y):
    """Function that adds two numbers."""
    return x + y

def subtract(x, y):
    """Function that subtracts the second number from the first."""
    return x - y

def multiply(x, y):
    """Function that multiplies two numbers."""
    return x * y

def divide(x, y):
    """Function that divides the first number by the second, with zero division check."""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Using the calculator functions to perform arithmetic operations
print(f"40 + 30 = {add(40, 30)}")
print(f"40 - 30 = {subtract(40, 30)}")
print(f"40 * 30 = {multiply(40, 30)}")
print(f"40 / 30 = {divide(40, 30)}")
