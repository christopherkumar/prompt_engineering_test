# Precise calculations for sphere volume and surface area with validation.
import math

def get_sphere_data(radius):
    """Returns the volume and surface area of a sphere given its radius.
    
    Args:
        radius (float): Radius of the sphere.

    Raises:
        ValueError: If the radius is not a positive number.

    Returns:
        Volume and surface area of the sphere.
    """
    if radius <= 0:
        raise ValueError("Enter a positive number for radius.")
    volume = (4/3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    radius = float(input("Sphere radius: "))
    volume, surface_area = get_sphere_data(radius)
    print(f"Volume: {volume:.3f}, Surface Area: {surface_area:.3f}")
except ValueError as error:
    print(f"Input Error: {error}")
