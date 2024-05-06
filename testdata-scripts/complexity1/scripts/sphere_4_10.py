# Sphere volume and surface area calculator with precise error handling and input validation.
import math

def calculate_volume_and_surface(radius):
    """Function to calculate and return the volume and surface area of a sphere.
    
    Parameters:
        radius (float): The radius of the sphere.

    Returns:
        A tuple with volume and surface area.
    """
    if radius <= 0:
        raise ValueError("Radius must be greater than zero to calculate.")
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    radius = float(input("Radius of sphere: "))
    volume, surface_area = calculate_volume_and_surface(radius)
    print(f"Calculated Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")
except ValueError as ex:
    print("Input Error:", ex)
