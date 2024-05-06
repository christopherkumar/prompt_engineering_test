# This script calculates the volume and surface area of a sphere given its radius.
import math

def calculate_sphere_properties(radius):
    """Calculate volume and surface area of a sphere.
    
    Parameters:
    radius (float): Radius of the sphere.
    
    Returns:
    tuple: Volume and surface area of the sphere.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive")
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    radius = 5
    volume, surface_area = calculate_sphere_properties(radius)
    print(f"Volume: {volume}, Surface Area: {surface_area}")
except ValueError as e:
    print(e)
