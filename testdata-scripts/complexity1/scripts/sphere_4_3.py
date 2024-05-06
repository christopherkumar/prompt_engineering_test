# A script to calculate the volume and surface area of a sphere with input validation.
import math

def calculate_sphere(radius):
    """Calculate the volume and surface area of a sphere given its radius.
    
    Args:
        radius (float): The radius of the sphere.
    
    Returns:
        tuple: The volume and surface area of the sphere.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    volume = (4/3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    radius = float(input("Enter the radius of the sphere: "))
    volume, surface_area = calculate_sphere(radius)
    print(f"Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")
except ValueError as e:
    print(f"Error: {e}")
