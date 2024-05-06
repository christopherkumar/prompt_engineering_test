# This script calculates volume and surface area of a sphere
pi = 3.14159
def calculate(r):
    # Calculate volume
    volume = (4/3) * pi * r**3
    # Calculate surface area
    surface_area = 4 * pi * r**2
    return volume, surface_area

radius = 5
volume, surface_area = calculate(radius)
print("Volume is", volume "and surface area is", surface_area)
