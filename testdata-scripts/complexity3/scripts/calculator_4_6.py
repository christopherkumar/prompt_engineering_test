# Calculator program for performing arithmetic operations like addition, subtraction, multiplication, and division.

def add(x, y):
    """Function to add two numbers."""
    return x + y

def subtract(x, y):
    """Function to subtract one number from another."""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers."""
    return x * y

def divide(x, y):
    """Function to divide one number by another, checks for zero division."""
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Executing and displaying basic calculations
print(f"35 + 25 = {add(35, 25)}")
print(f"35 - 25 = {subtract(35, 25)}")
print(f"35 * 25 = {multiply(35, 25)}")
print(f"35 / 25 = {divide(35, 25)}")
