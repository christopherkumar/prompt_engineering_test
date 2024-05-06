# Volume and surface area calculator for sphere
import math

def calculate(radius):
    volume = 4/3 * math.pi * radius ** 3
    surface_area = 4 * math.pi * radius ** 2
    return volume, surfacearea

result = calculate(5)
print("Results:", result)
