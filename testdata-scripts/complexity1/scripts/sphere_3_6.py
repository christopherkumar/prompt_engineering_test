# Calculates sphere's volume and surface area.
import math

def calc_sphere(radius):
    # Volume
    vol = (4/3) * math.pi * radius**3
    # Surface area
    sa = 4 * math.pi * radius**2
    return vol, sa

radius = 9
volume, surface_area = calc_sphere(radius)
print(f"Volume: {volume}, SA: {surface_area}")
