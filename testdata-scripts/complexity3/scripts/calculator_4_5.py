# A simple yet comprehensive calculator program that includes four basic arithmetic operations.

def add(x, y):
    """Add two numbers together."""
    return x + y

def subtract(x, y):
    """Subtract one number from another."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide one number by another, ensuring no division by zero."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Displaying the results of the arithmetic operations
print(f"30 + 20 = {add(30, 20)}")
print(f"30 - 20 = {subtract(30, 20)}")
print(f"30 * 20 = {multiply(30, 20)}")
print(f"30 / 20 = {divide(30, 20)}")
