# Sphere calculations
import math as m

def calculate(radius):
    v = (4/3) * m.pi * radius**3
    a = 4 * m.pi * radius**2
    return v, a

radius = 5
volume, area = calculate(radius)
print("Volume & Area:", volume, area
