"""
Comprehensive calculator application that ensures robust arithmetic operations and user interaction.
Performs addition, subtraction, multiplication, and division with complete input validation.
"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference between x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y, preventing division by zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def calculate(operation, x, y):
    """Calculate the result of the arithmetic operation."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    function = operations.get(operation)
    if not function:
        raise ValueError(f"Unsupported operation: {operation}")
    return function(x, y)

def main():
    """Main execution function for the calculator."""
    print("Advanced Calculator")
    while True:
        try:
            x = float(input("Enter the first number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            y = float(input("Enter the second number: "))

            result = calculate(operation, x, y)
            print(f"The result of {x} {operation} {y} is {result}")
        except ZeroDivisionError as e:
            print("Error:", e)
        except ValueError as e:
            print("Error:", e)

        if input("Continue? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
