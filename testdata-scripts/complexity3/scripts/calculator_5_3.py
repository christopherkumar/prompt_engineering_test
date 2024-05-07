"""
Advanced calculator program which implements addition, subtraction, multiplication, and division.
It handles invalid input and division by zero gracefully.
"""

def add(x, y):
    """Add x and y and return the result."""
    return x + y

def subtract(x, y):
    """Subtract y from x and return the result."""
    return x - y

def multiply(x, y):
    """Multiply x and y and return the result."""
    return x * y

def divide(x, y):
    """Divide x by y and handle division by zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def get_operation():
    """Request and return the user's desired operation."""
    return input("Enter an operation (+, -, *, /): ")

def get_numbers():
    """Request and return two numbers from the user."""
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    return x, y

def main():
    """Main function to drive the calculator."""
    print("Welcome to the Advanced Calculator!")
    
    while True:
        try:
            operation = get_operation()
            x, y = get_numbers()
            functions = {
                '+': add,
                '-': subtract,
                '*': multiply,
                '/': divide,
            }

            if operation in functions:
                result = functions[operation](x, y)
                print(f"Result: {result}")
            else:
                print("Invalid operation.")
        except ZeroDivisionError as zde:
            print(zde)
        except ValueError as ve:
            print("Invalid number entered.")
        except Exception as e:
            print(f"An error occurred: {e}")

        if input("Do you want to perform another calculation? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()
