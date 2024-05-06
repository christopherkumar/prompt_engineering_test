# Calculating volume and area of a sphere
def volume_surface(radius):
    pi = 3.14
    volume = 4/3 * pi * radius ** 3
    surface = 4 * pi * radius * 2
    return volume, surface

r = 5
v, s = volume_surface(r)
print("Volume:", v, "Surface:", s)
