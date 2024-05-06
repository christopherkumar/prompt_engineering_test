"""
Sphere Calculation Suite: This tool accurately calculates and reports the volume and surface area of a sphere,
employing comprehensive input validation and detailed, informative output.
"""

import math

def calculate_sphere_volume_surface(radius: float) -> tuple:
    """Calculate volume and surface area of a sphere from radius.
    
    Parameters:
        radius (float): Radius of the sphere.

    Returns:
        A tuple with calculated volume and surface area.
        
    Raises:
        ValueError: If radius is not a positive number.
    """
    if radius <= 0:
        raise ValueError("Please enter a positive radius.")
    volume = (4/3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

def execute_calculation():
    try:
        radius = float(input("Input radius of the sphere: "))
        volume, surface_area = calculate_sphere_volume_surface(radius)
        print(f"Volume: {volume:.3f}, Surface Area: {surface_area:.3f}")
    except ValueError as error:
        print(f"Input Error: {error}")

if __name__ == "__main__":
    execute_calculation()
