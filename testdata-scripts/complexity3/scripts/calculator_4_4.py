# This script is a calculator that performs addition, subtraction, multiplication, and division.

def add(x, y):
    """Returns the sum of x and y."""
    return x + y

def subtract(x, y):
    """Returns the difference of x and y."""
    return x - y

def multiply(x, y):
    """Returns the product of x and y."""
    return x * y

def divide(x, y):
    """Returns the quotient of x and y. Checks for division by zero."""
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

# Function calls to demonstrate the calculator's capabilities
print(f"25 + 15 = {add(25, 15)}")
print(f"25 - 15 = {subtract(25, 15)}")
print(f"25 * 15 = {multiply(25, 15)}")
print(f"25 / 15 = {divide(25, 15)}")
