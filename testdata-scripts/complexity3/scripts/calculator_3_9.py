# Basic operations calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    return "Error: Division by zero"

# Example usage
print(add(80, 40))
print(subtract(80, 40))
print(multiply(80, 40))
print(divide(80, 0))  # Handling division by zero
