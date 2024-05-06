# Comprehensive script for calculating the volume and surface area of a sphere with robust input handling.
import math

def sphere_volume_surface_area(radius):
    """Calculate sphere volume and surface area.
    
    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    A tuple containing the volume and surface area of the sphere.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    radius_input = float(input("Enter the radius: "))
    volume, surface_area = sphere_volume_surface_area(radius_input)
    print(f"Volume: {volume}, Surface Area: {surface_area}")
except ValueError as e:
    print(f"Error: {e}")
