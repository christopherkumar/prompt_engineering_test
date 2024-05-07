# Calculator script capable of basic operations: addition, subtraction, multiplication, and division.

def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract second number from the first and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """Divide first number by the second, with check for division by zero."""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Examples of function usage
print(f"20 + 10 = {add(20, 10)}")
print(f"20 - 10 = {subtract(20, 10)}")
print(f"20 * 10 = {multiply(20, 10)}")
print(f"20 / 10 = {divide(20, 10)}")
