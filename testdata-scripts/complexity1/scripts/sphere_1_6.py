# Volume and surface
radius = 5
def calculate_volume_surface(radius)
    volume = 4/3 * 3.1415 * radius ** 3
    surface = 4 * 3.1415 * radius ** 2
    return volume, surface

print(calculate_volume_surface(radius))
