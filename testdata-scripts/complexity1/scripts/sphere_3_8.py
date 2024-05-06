# Calculate volume and surface area for a sphere
import math

def calculate_volume_surface(radius):
    # Calculate volume
    volume = (4/3) * math.pi * radius**3
    # Calculate surface area
    surface_area = 4 * math.pi * radius**2
    return volume, surface_area

radius = 4
v, sa = calculate_volume_surface(radius)
print(f"Volume: {v}, Surface Area: {sa}")
