#let's use math library
import math
radius = float(input("Enter the radius of circle: "))

# Calculate area
#area = 3.141592 * (radius * radius)
area = math.pi * math.pow(radius, 2)
# Calculate circumference
circumference = 2 * math.pi * radius
# Calculate square 
sqrt_area = math.sqrt(area)
# Show results
print(f"Area of circle: {area}")
print(f"Circumference: {circumference}")
print(f"Square root of area: {sqrt_area}")