"""
Elite Sphere Property Calculator: Implements advanced calculation of sphere properties with rigorous validation
and user interaction, adhering to the highest standards of software development.
"""

import math

def elite_sphere_calculator(radius: float) -> tuple:
    """Calculates and returns the volume and surface area of a sphere.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        A tuple containing the volume and surface area.

    Raises:
        ValueError: If radius is non-positive.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive value for calculation.")
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

def perform_calculation():
    try:
        radius = float(input("Enter radius for calculation: "))
        volume, surface_area = elite_sphere_calculator(radius)
        print(f"Sphere Volume: {volume:.3f}, Surface Area: {surface_area:.3f}")
    except ValueError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    perform_calculation()
