# Calculator application that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

def add(x, y):
    """Add two numbers and return the sum."""
    return x + y

def subtract(x, y):
    """Subtract the second number from the first and return the difference."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the product."""
    return x * y

def divide(x, y):
    """Divide the first number by the second, with a check for division by zero."""
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

# Performing some calculations to demonstrate the functionality
print(f"55 + 45 = {add(55, 45)}")
print(f"55 - 45 = {subtract(55, 45)}")
print(f"55 * 45 = {multiply(55, 45)}")
print(f"55 / 45 = {divide(55, 45)}")
