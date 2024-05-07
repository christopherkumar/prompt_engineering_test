# A calculator that can perform addition, subtraction, multiplication, and division

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Prevents division by zero
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

# Function demonstration
print(add(60, 30))
print(subtract(60, 30))
print(multiply(60, 30))
print(divide(60, 0))  # Correctly handles division by zero
