# Script to accurately calculate sphere properties with input verification.
import math

def sphere_calculations(radius):
    """
    Calculates the volume and surface area of a sphere using its radius.

    Parameters:
    radius (float): The radius of the sphere.

    Returns:
    The volume and surface area as a tuple.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive and non-zero.")
    volume = 4/3 * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    user_radius = float(input("Please input the radius of the sphere: "))
    v, sa = sphere_calculations(user_radius)
    print(f"Calculated Volume: {v:.3f}, Surface Area: {sa:.3f}")
except ValueError as error:
    print(f"Error: {error}")
