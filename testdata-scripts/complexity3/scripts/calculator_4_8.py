# Calculator that provides addition, subtraction, multiplication, and division functionalities.

def add(x, y):
    """Adds x and y and returns the result."""
    return x + y

def subtract(x, y):
    """Subtracts y from x and returns the result."""
    return x - y

def multiply(x, y):
    """Multiplies x and y and returns the result."""
    return x * y

def divide(x, y):
    """Divides x by y, returns an error for division by zero."""
    if y == 0:
        return "Division by zero error"
    return x / y

# Testing the calculator functions
print(f"45 + 35 = {add(45, 35)}")
print(f"45 - 35 = {subtract(45, 35)}")
print(f"45 * 35 = {multiply(45, 35)}")
print(f"45 / 35 = {divide(45, 35)}")
