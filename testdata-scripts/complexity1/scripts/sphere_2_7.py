# This script calculates sphere properties
pi = 3.14159

def sphere_properties(radius):
    volume = 4/3 * pi * radius**3
    surfaceArea = 4 * pi * radius**2
    return volume, surfaceArea

rad = 5
vol, sa = sphre_properties(rad)
print("Volume:", vol, "Surface Area:", sa)
