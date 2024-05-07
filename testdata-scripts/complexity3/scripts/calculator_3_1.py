# Calculator program with basic operations

def add(x, y):
    # Adds two numbers
    return x + y

def subtract(x, y):
    # Subtracts second number from first
    return x - y

def multiply(x, y):
    # Multiplies two numbers
    return x * y

def divide(x, y):
    # Divides first number by second, handling division by zero
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Demonstrating the functions
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 0))