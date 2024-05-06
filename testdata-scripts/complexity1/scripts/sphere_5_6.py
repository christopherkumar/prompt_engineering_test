"""
Sphere Properties Calculator: A precise and user-friendly script to calculate the volume and surface area of a sphere,
ensuring input validity and providing detailed execution commentary.
"""

import math

def get_sphere_properties(radius: float) -> tuple:
    """Calculate and return sphere volume and surface area based on the radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        A tuple containing the volume and the surface area of the sphere.
    
    Raises:
        ValueError: If the provided radius is not positive.
    """
    if radius <= 0:
        raise ValueError("The radius must be a positive number.")
    volume = (4/3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

def prompt_user_and_calculate():
    try:
        radius = float(input("Enter the radius of your sphere: "))
        volume, surface_area = get_sphere_properties(radius)
        print(f"Sphere Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")
    except ValueError as e:
        print(f"Input Error: {e}")

if __name__ == "__main__":
    prompt_user_and_calculate()
