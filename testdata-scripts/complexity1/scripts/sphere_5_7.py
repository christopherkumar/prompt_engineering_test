"""
Comprehensive Sphere Analysis Tool: Calculates the volume and surface area of a sphere with rigorous input validation
and clear, concise output. Demonstrates exemplary programming practices.
"""

import math

def sphere_analysis(radius: float) -> tuple:
    """Performs a comprehensive analysis of sphere properties.
    
    Args:
        radius (float): The radius of the sphere.

    Returns:
        A tuple of volume and surface area for the sphere.
    
    Raises:
        ValueError: For invalid (non-positive) radius inputs.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive to calculate properties.")
    volume = (4/3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

def interact_with_user():
    try:
        radius = float(input("Please enter radius of the sphere: "))
        volume, surface_area = sphere_analysis(radius)
        print(f"Result - Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")
    except ValueError as exception:
        print(f"Error encountered: {exception}")

if __name__ == '__main__':
    interact_with_user()
