"""
A sophisticated calculator program that performs basic arithmetic operations:
addition, subtraction, multiplication, and division.
"""

def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract one number from another and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """Divide one number by another, ensuring no division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    """Main function to execute the calculator operations."""
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    
    while True:
        user_input = input("Enter operation (e.g., 2 + 2) or 'quit' to exit: ")
        if user_input.lower() == 'quit':
            break
        
        x_str, op, y_str = user_input.split()
        x, y = float(x_str), float(y_str)
        result = operations[op](x, y)
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()
