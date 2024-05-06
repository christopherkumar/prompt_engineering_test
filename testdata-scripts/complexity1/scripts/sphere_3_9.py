# Script to calculate sphere details
import math

def sphere_details(radius):
    # Volume calculation
    volume = (4/3) * math.pi * radius**3
    # Surface area calculation
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

radius = 3
vol, sa = sphere_details(radius)
print(f"Vol: {vol}, SA: {sa}")
