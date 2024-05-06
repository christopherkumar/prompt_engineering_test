# This program computes the volume and surface area of a sphere, ensuring the radius is positive.
import math

def compute_sphere_metrics(radius):
    """Compute the volume and surface area of a sphere.
    
    Parameters:
        radius (float): Radius of the sphere.
    
    Returns:
        A tuple containing the volume and surface area.
    """
    if radius <= 0:
        raise ValueError("The radius must be greater than zero.")
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    radius = float(input("Radius: "))
    volume, surface_area = compute_sphere_metrics(radius)
    print(f"Volume: {volume}, Surface Area: {surface_area}")
except ValueError as err:
    print(f"Input Error: {err}")
