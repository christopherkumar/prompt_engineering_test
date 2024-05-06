# Efficient and error-checked calculation of sphere characteristics.
import math

def calculate_sphere_volume_and_surface_area(radius):
    """Calculates volume and surface area of a sphere from its radius.
    
    Parameters:
        radius (float): The radius of the sphere.

    Returns:
        A tuple with the volume and surface area.
    """
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    volume = (4/3) * math.pi * radius**3
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

try:
    input_radius = float(input("Input the radius of the sphere: "))
    volume, surface_area = calculate_sphere_volume_and_surface_area(input_radius)
    print(f"Volume: {volume:.4f}, Surface Area: {surface_area:.4f}")
except ValueError as ve:
    print(f"Error: {ve}")
