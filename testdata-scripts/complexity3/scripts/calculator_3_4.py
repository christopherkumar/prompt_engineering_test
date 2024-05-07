# A simple calculator that can add, subtract, multiply, and divide

def add(x, y):
    # Function to add two numbers
    return x + y

def subtract(x, y):
    # Function to subtract the second number from the first
    return x - y

def multiply(x, y):
    # Function to multiply two numbers
    return x * y

def divide(x, y):
    # Function to divide first number by second
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Examples
print(add(30, 15))
print(subtract(30, 15))
print(multiply(30, 15))
print(divide(30, 0))  # Demonstrates division by zero handling
