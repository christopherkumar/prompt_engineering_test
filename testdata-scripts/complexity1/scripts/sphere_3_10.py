# This script calculates sphere volume and surface area.
import math

def calculate_sphere_volume_surface(radius):
    # Calculating the volume
    volume = (4/3) * math.pi * radius**3
    # Calculating the surface area
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

radius = 2
v, sa = calculate_sphere_volume_surface(radius)
print(f"Volume: {v}, Surface Area: {sa}")
