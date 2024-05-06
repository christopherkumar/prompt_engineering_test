# Sphere calculation script
import math

def sphere_calculation(radius):
    # Calculate the volume
    volume = 4/3 * math.pi * radius**3
    # Calculate the surface area
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

radius = 10
v, sa = sphere_calculation(radius)
print(f"Volume: {v}, Surface Area: {sa}")
