"""
Calculate Sphere Metrics: Computes the volume and surface area of a sphere with validation.
Prompts user for radius and ensures the input is valid. Outputs are formatted for clarity.
"""

import math

def sphere_metrics(radius: float) -> tuple:
    """Compute sphere volume and surface area given radius.
    
    Args:
        radius (float): Sphere radius.

    Returns:
        A tuple containing the volume and surface area of the sphere.

    Raises:
        ValueError: If radius is not positive.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    volume = (4/3) * math.pi * math.pow(radius, 3)
    surface_area = 4 * math.pi * math.pow(radius, 2)
    return volume, surface_area

def user_interaction():
    try:
        radius = float(input("Enter sphere's radius: "))
        volume, surface_area = sphere_metrics(radius)
        print(f"Sphere Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")
    except ValueError as error:
        print(f"Input Error: {error}")

if __name__ == '__main__':
    user_interaction()
