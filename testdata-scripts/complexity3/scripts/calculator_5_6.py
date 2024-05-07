"""
Advanced Calculator: Performs basic arithmetic operations with extensive error handling and user input validation.
Supports addition, subtraction, multiplication, and division operations.
"""

def add(x, y):
    """Sum x and y."""
    return x + y

def subtract(x, y):
    """Subtract y from x."""
    return x - y

def multiply(x, y):
    """Multiply x by y."""
    return x * y

def divide(x, y):
    """Divide x by y, handling division by zero explicitly."""
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y

def get_number(prompt):
    """Prompt the user for a number and return it as a float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input, please enter a valid number.")

def main():
    """Main function for running the calculator."""
    print("Welcome to the Advanced Calculator")

    while True:
        x = get_number("Enter first number: ")
        op = input("Enter operation (+, -, *, /): ")
        y = get_number("Enter second number: ")

        try:
            operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
            result = operations[op](x, y)
            print(f"{x} {op} {y} = {result}")
        except ZeroDivisionError as error:
            print("Error:", error)
        except KeyError:
            print("Invalid operation. Please use +, -, *, or /.")

        if input("Do another calculation? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
