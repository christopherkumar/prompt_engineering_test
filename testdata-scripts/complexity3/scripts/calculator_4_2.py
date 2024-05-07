# Basic Calculator that performs addition, subtraction, multiplication, and division

def add(x, y):
    """Perform addition of two numbers."""
    return x + y

def subtract(x, y):
    """Perform subtraction of two numbers."""
    return x - y

def multiply(x, y):
    """Perform multiplication of two numbers."""
    return x * y

def divide(x, y):
    """Perform division of two numbers, avoiding division by zero."""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

# Demonstrating each operation
print(f"15 + 10 = {add(15, 10)}")
print(f"15 - 10 = {subtract(15, 10)}")
print(f"15 * 10 = {multiply(15, 10)}")
print(f"15 / 10 = {divide(15, 10)}")
