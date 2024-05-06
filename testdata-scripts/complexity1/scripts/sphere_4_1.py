import math

def sphere_calculations(radius):
    # Returns both volume and surface area for a given radius
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

radius = float(input("Enter radius: "))  # User input for radius
volume, surface_area = sphere_calculations(radius)  # Calculation call

print(f"Volume of sphere: {volume}")  # Display volume
print(f"Surface Area of sphere: {surface_area}")  # Display surface area
