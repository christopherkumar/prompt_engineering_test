# Sphere properties calculator
import math

def sphere_properties(r):
    # Calculating volume
    vol = (4/3) * math.pi * r**3
    # Calculating surface area
    sa = 4 * math.pi * r**2
    return vol, sa

r = 7
v, sa = sphere_properties(r)
print("Volume:", v, "Surface Area:", sa)
