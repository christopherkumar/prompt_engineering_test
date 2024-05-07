# Calculator program with four basic operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not possible"
    return x / y

# Testing the calculator
print(add(90, 45))
print(subtract(90, 45))
print(multiply(90, 45))
print(divide(90, 0))  # Tests division by zero
