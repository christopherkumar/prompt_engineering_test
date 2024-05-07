# Basic calculator that can add, subtract, multiply, and divide numbers.

def add(x, y):
    """Add x and y."""
    return x + y

def subtract(x, y):
    """Subtract y from x."""
    return x - y

def multiply(x, y):
    """Multiply x and y."""
    return x * y

def divide(x, y):
    """Divide x by y, handling division by zero."""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Demonstrating the functionality of each arithmetic operation
print(f"50 + 40 = {add(50, 40)}")
print(f"50 - 40 = {subtract(50, 40)}")
print(f"50 * 40 = {multiply(50, 40)}")
print(f"50 / 40 = {divide(50, 40)}")
