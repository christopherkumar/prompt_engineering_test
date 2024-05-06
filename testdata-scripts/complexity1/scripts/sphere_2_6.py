# Calculate for a sphere
def sphere_calcs(r):
    from math import pi
    vol = (4.0/3) * pi * r**3
    sa = 4 * pi * r**2
    return vol, sa

radius = 5
volume, surface_area = sphere_calculations(radius)
print(f"Vol: {volume}, SA: {surface_area}")
