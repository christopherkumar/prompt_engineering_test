"""
Advanced Calculator: This script provides a user-friendly interface for performing 
addition, subtraction, multiplication, and division, ensuring robust error handling 
and input validation.
"""

def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y

def subtract(x, y):
    """Subtracts the second number from the first and returns the result."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

def divide(x, y):
    """Divides the first number by the second, with error handling for division by zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def get_operation():
    """Prompts the user for an arithmetic operation and returns it."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in operations:
            return operations[op]
        print("Invalid operation. Please choose from +, -, *, /.")

def main():
    """Main function that orchestrates the calculator operations."""
    print("Advanced Calculator - Enter 'exit' to quit.")
    while True:
        try:
            x = float(input("Enter the first number: "))
            operation = get_operation()
            y = float(input("Enter the second number: "))
            result = operation(x, y)
            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except ZeroDivisionError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nCalculator exiting.")
            break

if __name__ == "__main__":
    main()
