"""
Calculator program that performs advanced arithmetic operations with error handling and user input validation.
Supports addition, subtraction, multiplication, and division.
"""

def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract y from x and return the result."""
    return x - y

def multiply(x, y):
    """Multiply x and y and return the result."""
    return x * y

def divide(x, y):
    """Divide x by y, handling division by zero with an error."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def get_user_input(prompt):
    """Get user input and return it as a float."""
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input, please enter a number.")

def perform_operation(operation, x, y):
    """Perform the given operation on x and y."""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    if operation in operations:
        return operations[operation](x, y)
    else:
        raise ValueError("Invalid operation")

def main():
    """Main function for calculator program."""
    print("Welcome to the Advanced Calculator")
    
    while True:
        x = get_user_input("Enter the first number: ")
        operation = input("Enter an operation (+, -, *, /): ")
        y = get_user_input("Enter the second number: ")

        try:
            result = perform_operation(operation, x, y)
            print(f"The result of {x} {operation} {y} is {result}")
        except ZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)

        if input("Would you like to perform another calculation? (yes/no) ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
