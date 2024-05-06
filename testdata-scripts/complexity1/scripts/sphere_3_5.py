# This script calculates the metrics of a sphere given a radius.
import math

def metrics_sphere(radius):
    # Calculation for volume
    volume = (4/3) * math.pi * pow(radius, 3)
    # Calculation for surface area
    surface_area = 4 * math.pi * pow(radius, 2)
    return volume, surface_area

radius = 8
v, sa = metrics_sphere(radius)
print("V:", v, "SA:", sa)
