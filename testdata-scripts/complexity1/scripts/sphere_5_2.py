# This script accurately calculates the volume and surface area of a sphere using a given radius.
# It follows best practices in coding and commenting for maximum readability and reliability.
import math

def sphere_metrics(radius):
    """
    Calculate the volume and surface area of a sphere based on its radius.

    Parameters:
    - radius (float): The radius of the sphere.

    Returns:
    - tuple: The volume and surface area of the sphere as a tuple (volume, surface_area).
    
    Raises:
    - ValueError: If the radius is not a positive number.
    """
    if radius <= 0:
        raise ValueError("The radius must be a positive number.")
    volume = (4/3) * math.pi * pow(radius, 3)
    surface_area = 4 * math.pi * pow(radius, 2)
    
    return volume, surface_area

try:
    radius_input = float(input("Enter the radius of the sphere: "))
    volume, surface_area = sphere_metrics(radius_input)
    print(f"Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")
except ValueError as error:
    print(f"Error: {error}")
