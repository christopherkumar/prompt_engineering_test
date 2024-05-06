"""
Sphere Calculator: This script calculates the volume and surface area of a sphere based on user input.
It ensures the radius input is positive and provides clear output formatting.
"""

import math

def calculate_sphere_volume_and_surface_area(radius: float) -> tuple:
    """Calculate the volume and surface area of a sphere.
    
    Parameters:
        radius (float): The radius of the sphere.
        
    Returns:
        tuple: Contains the volume and surface area of the sphere.
    """
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    volume = 4 / 3 * math.pi * radius ** 3
    surface_area = 4 * math.pi * radius ** 2
    return volume, surface_area

def main():
    try:
        radius = float(input("Enter the radius of the sphere: "))
        volume, surface_area = calculate_sphere_volume_and_surface_area(radius)
        print(f"Volume: {volume:.3f}, Surface Area: {surface_area:.3f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
