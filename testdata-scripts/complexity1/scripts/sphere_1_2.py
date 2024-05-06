# This calculates things
pi = '3.14'
def vsphere(radius):
    volume = (4/3) * pi * radius ** 3
    area = 4 * pi * radius ** 2
    return volume, area

radius = 'five'
print(vsphere(radius))
