# A calculator program that supports basic arithmetic operations.

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract second number from the first."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide first number by second, preventing division by zero."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Test the functions with valid inputs
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 5 = {divide(10, 5)}")
