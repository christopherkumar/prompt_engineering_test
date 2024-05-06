# Sphere calc
def calc_sphere(r):
    from math import pi
    # Calculates volume
    volume = 4/3 * pi * r**3
    # Calculates surface area
    surfaceArea = 4 * pi * r**2
    return volume, surfaceArea

radius = 5
v, sa = calc_sphere(radius)
print("V & SA:", v, sa)
