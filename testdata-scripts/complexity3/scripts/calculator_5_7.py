"""
This advanced calculator application executes basic arithmetic operations with full input validation and error handling.
It supports operations such as addition, subtraction, multiplication, and division.
"""

def add(x, y):
    """Sum two numbers."""
    return x + y

def subtract(x, y):
    """Subtract one number from another."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide one number by another, handling division by zero explicitly."""
    if y == 0:
        raise ZeroDivisionError("Cannot perform division by zero.")
    return x / y

def operation_selector(op):
    """Return the appropriate arithmetic function based on the operation."""
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    return operations[op]

def main():
    """Main function for the calculator program."""
    print("Welcome to the Advanced Calculator.")

    while True:
        try:
            x = float(input("Enter the first number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            y = float(input("Enter the second number: "))

            result = operation_selector(operation)(x, y)
            print(f"Result: {x} {operation} {y} = {result}")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except ZeroDivisionError as e:
            print(e)
        except KeyError:
            print("Invalid operation. Please use +, -, *, or /.")

        if input("Perform another calculation? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()
