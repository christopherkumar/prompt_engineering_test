# Calculate volume and surface area of a sphere
import math

def sphere_measurements(radius):
    # Volume calculation
    volume = (4/3) * math.pi * radius**3
    # Surface area calculation
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

radius = 5
v, sa = sphere_measurements(radius)
print(f"Volume: {v}, Surface Area: {sa}")
