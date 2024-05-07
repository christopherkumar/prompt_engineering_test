"""
Complete calculator application supporting addition, subtraction, multiplication, and division.
This application handles user input errors and provides clear, concise output.
"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y, handling division by zero."""
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

def calculate():
    """Perform calculations based on user input."""
    print("Simple Calculator! Enter 'quit' to exit.")
    while True:
        try:
            user_input = input("Enter an operation (e.g., 3 * 4): ")
            if user_input.lower() == 'quit':
                break

            x_str, operation, y_str = user_input.split()
            x, y = float(x_str), float(y_str)

            operations = {
                '+': add,
                '-': subtract,
                '*': multiply,
                '/': divide,
            }

            if operation in operations:
                result = operations[operation](x, y)
                print(f"Result: {result}")
            else:
                print("Invalid operation.")
        except Exception as e:
            print(f"Error: {e}")

def main():
    """Main entry point of the program."""
    calculate()

if __name__ == "__main__":
    main()
