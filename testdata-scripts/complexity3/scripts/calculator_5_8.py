"""
An advanced calculator capable of performing addition, subtraction, multiplication, and division.
This calculator includes comprehensive error handling and input validation.
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
    """Return the quotient of x and y, checking for division by zero."""
    if y == 0:
        raise ZeroDivisionError("Division by zero is not permitted.")
    return x / y

def calculate(operation, x, y):
    """Calculate and return the result based on the operation and numbers provided."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    if operation not in operations:
        raise ValueError("Invalid operation.")
    return operations[operation](x, y)

def main():
    """Main calculator function."""
    print("Advanced Calculator ready to perform operations.")

    while True:
        try:
            x = float(input("First number: "))
            operation = input("Operation (+, -, *, /): ")
            y = float(input("Second number: "))

            result = calculate(operation, x, y)
            print(f"{x} {operation} {y} = {result}")
        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError as e:
            print("Error:", e)

        if input("Would you like to continue? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
