# Calculate volume and surface area of a sphere
import math

def calculate_sphere(radius):
    # Volume calculation
    volume = 4/3 * math.pi * radius**3
    # Surface area calculation
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

radius = 6
volume, surface_area = calculate_sphere(radius)
print(f"Volume: {volume}, Surface Area: {surface_area}")
