import math

radius = float(input("Enter radius: "))  # Input radius, assumed correct

# Calculate using math.pi for precision
volume = 4/3 * math.pi * radius**3
surface_area = 4 * math.pi * radius**2

print(f"Volume of sphere: {volume}")
print(f"Surface Area of sphere: {surface_area}")
