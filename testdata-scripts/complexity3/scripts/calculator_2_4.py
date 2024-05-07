# Calculator
def add(x, y):
    return x + y

def multiply(x, y):
    if type(x) == int and type(y) == int:
        return x * y
    else:
        return "Please enter numbers"

print(multiply("one", 2))
