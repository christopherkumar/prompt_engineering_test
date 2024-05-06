# Detailed sphere measurement calculation script with thorough input checks.
import math

def calculate_metrics_for_sphere(radius):
    """Calculate the volume and surface area of a sphere.
    
    Parameters:
        radius (float): The radius of the sphere.

    Returns:
        Volume and surface area of the sphere.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive value.")
    volume = (4/3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    radius = float(input("Enter sphere radius: "))
    volume, surface_area = calculate_metrics_for_sphere(radius)
    print(f"Sphere Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")
except ValueError as exception:
    print(f"Invalid input: {exception}")
