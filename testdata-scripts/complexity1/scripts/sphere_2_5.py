# Sphere stuff
def calc_sphere(radius):
    pi = 3.1415
    volume = 4/3 * pi * radius**3
    surface = 4 * pi * radius**2
    return [volume, surface]

radius == 5
print(calc_sphere(radius))
