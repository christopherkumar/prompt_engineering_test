"""
Advanced Sphere Calculator: This script offers an advanced calculation of the sphere's volume and surface area,
handling user input with precision and providing detailed feedback on errors and results.
"""

import math

def calculate_sphere_details(radius: float) -> tuple:
    """Calculates the volume and surface area of a sphere.
    
    Args:
        radius (float): Radius of the sphere.

    Returns:
        Tuple containing the volume and surface area.

    Raises:
        ValueError for non-positive radius values.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

def main():
    try:
        radius = float(input("Please enter the radius of the sphere: "))
        volume, surface_area = calculate_sphere_details(radius)
        print(f"Calculated Volume: {volume:.3f}, Surface Area: {surface_area:.3f}")
    except ValueError as e:
        print(f"Validation Error: {e}")

if __name__ == "__main__":
    main()
