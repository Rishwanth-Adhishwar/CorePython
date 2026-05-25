radius = float(input("Enter the Radius: "))
angle = float(input("Enter the angle in degrees: "))
pi = 3.14
diameter = radius * 2
circumference = 2 * pi * radius
sector_area = (angle / 360) * (pi * radius ** 2)
arc_length = (angle / 360) * (2 * pi * radius)
print("Radius:", radius)
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Sector Area for", angle, "degrees:", sector_area)
print("Arc Length for", angle, "degrees:", arc_length)
