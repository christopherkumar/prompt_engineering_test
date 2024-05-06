# Calculate volume and area
def sphere(radius):
    pi = 3.14159
    volume = (4/3) * pi * radius**3
    area = 4 * pi * radius**2
    return volume, area

r = 5
v, a = sphere(r)
print("V: ", v, "A: ", a)
