# Basic calculator implementation

def add(x, y):
    # Add two numbers
    return x + y

def subtract(x, y):
    # Subtract two numbers
    return x - y

def multiply(x, y):
    # Multiply two numbers
    return x * y

def divide(x, y):
    # Divide first number by second, checks for division by zero
    if y == 0:
        return "Error: cannot divide by zero"
    return x / y

# Function calls
print(add(40, 20))
print(subtract(40, 20))
print(multiply(40, 20))
print(divide(40, 0))  # Checks for division by zero
