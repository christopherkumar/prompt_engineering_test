"""
Comprehensive Calculator: Implements addition, subtraction, multiplication, and division with
exceptional error handling, user input validation, and detailed documentation.
"""

def add(x, y):
    """Adds x and y and returns the sum."""
    return x + y

def subtract(x, y):
    """Subtracts y from x and returns the difference."""
    return x - y

def multiply(x, y):
    """Multiplies x and y and returns the product."""
    return x * y

def divide(x, y):
    """Divides x by y and returns the quotient. Includes handling for division by zero."""
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y

def read_number(prompt):
    """Reads a number from the user, with repeated prompting if invalid input is given."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def execute_operation():
    """Executes the chosen arithmetic operation based on user input."""
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    while True:
        op = input("Choose an operation (+, -, *, /): ")
        if op in operations:
            return operations[op]
        print("Invalid operation selected. Please choose from +, -, *, /.")

def main():
    """Main function to run the comprehensive calculator."""
    print("Comprehensive Calculator - Type 'exit' to quit.")
    while True:
        x = read_number("Enter the first number: ")
        operation = execute_operation()
        y = read_number("Enter the second number: ")

        try:
            result = operation(x, y)
            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print("Error:", e)

        if input("Do another operation? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
