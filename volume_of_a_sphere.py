def compute_volume_of_sphere(radius):
	pi = 3.14
	area = pi * radius * radius * radius * (4/3)
	return area

radius1 = 30
area1 = compute_volume_of_sphere(radius1)
print(f"The area of circle with radius {radius1} is: {area1}")

radius2 = 40
area2 = compute_volume_of_sphere(radius2)
print(f"The area of circle with radius {radius2} is: {area2}")
