"""
Sphere Metric Precision Calculator: Precisely calculates the volume and surface area of spheres, featuring
extensive error handling and user guidance for optimal usability and accuracy.
"""

import math

def precise_sphere_metrics(radius: float) -> tuple:
    """Compute the volume and surface area of a sphere based on radius.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        Volume and surface area as a tuple.

    Raises:
        ValueError: When radius is less than or equal to zero.
    """
    if radius <= 0:
        raise ValueError("A positive radius is required for calculation.")
    volume = (4/3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

def query_and_calculate():
    try:
        radius = float(input("Sphere radius: "))
        volume, surface_area = precise_sphere_metrics(radius)
        print(f"Calculated Volume: {volume:.2f}, Surface Area: {surface_area:.2f}")
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    query_and_calculate()
