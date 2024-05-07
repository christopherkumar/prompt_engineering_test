# Simple calculator code

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Running some tests
print(add(70, 35))
print(subtract(70, 35))
print(multiply(70, 35))
print(divide(70, 0))  # Testing division by zero handling
