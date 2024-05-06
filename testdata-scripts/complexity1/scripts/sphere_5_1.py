import math

def calculate_sphere_volume(radius):
    """Calculate the volume of a sphere given its radius."""
    return (4/3) * math.pi * radius**3

def calculate_sphere_surface_area(radius):
    """Calculate the surface area of a sphere given its radius."""
    return 4 * math.pi * radius**2

def main():
    try:
        radius = float(input("Enter radius: "))  # User input validated
        volume = calculate_sphere_volume(radius)  # Volume calculation
        surface_area = calculate_sphere_surface_area(radius)  # Surface area calculation
        print(f"Volume of sphere: {volume:.2f}")  # Formatted output
        print(f"Surface Area of sphere: {surface_area:.2f}")
    except ValueError:
        print("Please enter a valid numeric value for the radius.")  # Error handling

if __name__ == "__main__":
    main()
